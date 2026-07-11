(function () {
  "use strict";

  var WEIGHTS = {
    "Explains Algorithms": 0.29,
    "Determines Data Structure Impact": 0.31,
    "Applies Algorithms": 0.40
  };

  window.QuizEngine = {
    weights: WEIGHTS,
    createQuiz: createQuiz,
    grade: grade
  };

  function createQuiz(questions, count, focusTopics) {
    var pool = questions.slice();
    if (focusTopics && focusTopics.length) {
      pool = pool.filter(function (question) { return focusTopics.indexOf(question.topic) !== -1; });
    }
    return shuffle(pool).slice(0, Math.min(count || 20, pool.length));
  }

  function grade(questions, answers) {
    var competency = {};
    var topics = {};
    var review = questions.map(function (question) {
      var selected = answers[question.id];
      var correct = selected === question.answer;
      addResult(competency, question.competency, correct);
      addResult(topics, question.topic, correct);
      return { question: question, selected: selected, correct: correct };
    });

    var overall = Object.keys(WEIGHTS).reduce(function (score, name) {
      var result = competency[name] || { correct: 0, total: 0 };
      var percent = result.total ? result.correct / result.total : 0;
      return score + percent * WEIGHTS[name] * 100;
    }, 0);

    return {
      score: Math.round(overall),
      correct: review.filter(function (item) { return item.correct; }).length,
      total: questions.length,
      competency: withPercentages(competency),
      topics: withPercentages(topics),
      review: review,
      weakTopics: Object.keys(topics).filter(function (topic) { return topics[topic].correct / topics[topic].total < 0.7; })
    };
  }

  function addResult(collection, name, correct) {
    collection[name] = collection[name] || { correct: 0, total: 0 };
    collection[name].total += 1;
    collection[name].correct += correct ? 1 : 0;
  }

  function withPercentages(collection) {
    Object.keys(collection).forEach(function (name) {
      collection[name].percent = Math.round(collection[name].correct / collection[name].total * 100);
    });
    return collection;
  }

  function shuffle(items) {
    for (var index = items.length - 1; index > 0; index -= 1) {
      var target = Math.floor(Math.random() * (index + 1));
      var value = items[index];
      items[index] = items[target];
      items[target] = value;
    }
    return items;
  }
})();
