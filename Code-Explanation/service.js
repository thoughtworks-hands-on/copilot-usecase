async function processUserData() {
  try {
    const users = await fetchUsersFromServer();
    const userIDs = users.map(user => user.id);

    const promises = userIDs.map(async id => {
      const user = await fetchUserDetails(id);
      const userPosts = await fetchUserPosts(id);
      const postTitles = userPosts.map(post => post.title);

      return { user, postTitles };
    });

    const userPostData = await Promise.all(promises);

    const filteredUserData = userPostData.filter(data => data.user.isActive);
    const sortedUserData = filteredUserData.sort((a, b) => b.user.age - a.user.age);

    const summarizedData = sortedUserData.reduce((acc, data) => {
      acc[data.user.name] = data.postTitles;
      return acc;
    }, {});

    return summarizedData;
  } catch (error) {
    console.error("An error occurred:", error);
  }
}
