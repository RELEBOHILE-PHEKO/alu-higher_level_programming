#!/usr/bin/node
const request = require('request');

const apiUrl = process.argv[2];

request(apiUrl, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const todos = JSON.parse(body);
    const userTaskCounts = todos.reduce((counts, todo) => {
      if (todo.completed) {
        const userId = todo.userId;
        counts[userId] = (counts[userId] || 0) + 1;
      }
      return counts;
    }, {});

    console.log(userTaskCounts);
  }
});
