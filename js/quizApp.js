(function () {
  "use strict";

  var activeQuiz = [];
  var answers = {};
  var currentIndex = 0;
  var root = null;
  var STORAGE_KEY = "codeDeskQuizHistory";

  window.QuizApp = { open: open };

  function open() {
    root = document.createElement("div");
    root.className = "quiz-app";
    WindowManager.open({
      title: "C949 Quiz",
      content: root,
      width: "760px",
      height: "560px",
      minWidth: "520px",
      minHeight: "420px",
      className: "quiz-window",
      iconPath: "assets/icons/msg_information-2.png"
    });
    renderWelcome();
  }

  function renderWelcome() {
    root.innerHTML = "";
    var panel = element("section", "quiz-welcome");
    var title = element("h1", "", "Data Structures & Algorithms Quiz");
    var copy = element("p", "", "Answer 20 multiple-choice questions. Your results will identify the competencies and topics that need the most attention.");
    var details = element("ul", "quiz-summary-list");
    ["20 randomized questions", "Feedback after the final answer", "Weighted to the C949 competency distribution", "No time limit"].forEach(function (text) {
      details.appendChild(element("li", "", text));
    });
    var start = button("Start Quiz", startQuiz);
    panel.append(title, copy, details, start);
    appendHistory(panel);
    root.appendChild(panel);
  }

  function startQuiz(focusTopics) {
    activeQuiz = QuizEngine.createQuiz(QuizQuestions, 20, focusTopics);
    answers = {};
    currentIndex = 0;
    renderQuestion();
  }

  function renderQuestion() {
    var question = activeQuiz[currentIndex];
    root.innerHTML = "";
    var header = element("header", "quiz-header");
    var progressText = element("strong", "", "Question " + (currentIndex + 1) + " of " + activeQuiz.length);
    var topic = element("span", "quiz-topic", question.topic);
    var track = element("div", "quiz-progress");
    var fill = element("span", "quiz-progress-fill");
    fill.style.width = ((currentIndex + 1) / activeQuiz.length * 100) + "%";
    track.appendChild(fill);
    header.append(progressText, topic, track);

    var form = element("form", "quiz-question");
    var prompt = element("fieldset", "quiz-fieldset");
    var legend = element("legend", "quiz-prompt", question.prompt);
    prompt.appendChild(legend);
    question.choices.forEach(function (choice, index) {
      var label = element("label", "quiz-choice");
      var input = document.createElement("input");
      input.type = "radio";
      input.name = "quiz-answer";
      input.value = String(index);
      input.checked = answers[question.id] === index;
      label.append(input, element("span", "", choice));
      prompt.appendChild(label);
    });
    form.appendChild(prompt);

    var footer = element("footer", "quiz-actions");
    var back = button("< Back", function () { currentIndex -= 1; renderQuestion(); });
    var next = button(currentIndex === activeQuiz.length - 1 ? "Finish" : "Next >", function () {});
    back.disabled = currentIndex === 0;
    footer.append(back, next);
    form.appendChild(footer);
    form.addEventListener("submit", function (event) {
      event.preventDefault();
      var selected = form.querySelector('input[name="quiz-answer"]:checked');
      if (!selected) {
        showNotice("Choose an answer before continuing.");
        return;
      }
      answers[question.id] = Number(selected.value);
      if (currentIndex === activeQuiz.length - 1) renderResults();
      else { currentIndex += 1; renderQuestion(); }
    });
    next.type = "submit";
    root.append(header, form);
  }

  function renderResults() {
    var result = QuizEngine.grade(activeQuiz, answers);
    saveAttempt(result);
    root.innerHTML = "";
    var report = element("section", "quiz-results");
    var hero = element("header", "quiz-score-hero");
    var score = element("strong", "quiz-score", result.score + "%");
    var message = element("div", "");
    message.append(element("h1", "", scoreLabel(result.score)), element("p", "", result.correct + " of " + result.total + " questions correct"));
    hero.append(score, message);

    var competencyTitle = element("h2", "", "Competency breakdown");
    var competency = element("div", "quiz-breakdown");
    Object.keys(QuizEngine.weights).forEach(function (name) {
      competency.appendChild(resultRow(name, result.competency[name], Math.round(QuizEngine.weights[name] * 100) + "% of assessment"));
    });

    var topicTitle = element("h2", "", "Topic breakdown");
    var topics = element("div", "quiz-topic-grid");
    Object.keys(result.topics).sort(function (a, b) { return result.topics[a].percent - result.topics[b].percent; }).forEach(function (name) {
      topics.appendChild(resultRow(name, result.topics[name], ""));
    });

    var recommendation = element("section", "quiz-recommendation");
    recommendation.appendChild(element("h2", "", "What to work on"));
    recommendation.appendChild(element("p", "", result.weakTopics.length ? "Focus your next study session on: " + result.weakTopics.join(", ") + ". Review the missed-question explanations below, then practice those areas again." : "Strong result. Review any missed questions, then retake the full quiz to reinforce recall."));

    var actions = element("div", "quiz-actions");
    actions.append(button("New Quiz", function () { startQuiz(); }));
    if (result.weakTopics.length) actions.append(button("Practice Weak Areas", function () { startQuiz(result.weakTopics); }));

    var reviewTitle = element("h2", "", "Answer review");
    var review = element("div", "quiz-review");
    result.review.forEach(function (item, index) { review.appendChild(reviewItem(item, index)); });
    report.append(hero, competencyTitle, competency, topicTitle, topics, recommendation, actions, reviewTitle, review);
    root.appendChild(report);
  }

  function resultRow(name, result, note) {
    var row = element("div", "quiz-result-row");
    var label = element("div", "quiz-result-label");
    label.append(element("strong", "", name), element("small", "", note));
    var meter = element("div", "quiz-meter");
    var fill = element("span", "");
    fill.style.width = result.percent + "%";
    meter.appendChild(fill);
    row.append(label, meter, element("strong", "quiz-result-percent", result.percent + "%"));
    return row;
  }

  function reviewItem(item, index) {
    var section = element("section", "quiz-review-item " + (item.correct ? "is-correct" : "is-incorrect"));
    section.appendChild(element("h3", "", (index + 1) + ". " + item.question.prompt));
    section.appendChild(element("p", "", (item.correct ? "Correct: " : "Your answer: ") + item.question.choices[item.selected]));
    if (!item.correct) section.appendChild(element("p", "", "Correct answer: " + item.question.choices[item.question.answer]));
    section.appendChild(element("p", "quiz-explanation", item.question.explanation));
    return section;
  }

  function scoreLabel(score) {
    if (score >= 90) return "Excellent work";
    if (score >= 80) return "Good progress";
    if (score >= 70) return "On the right track";
    return "More practice recommended";
  }

  function showNotice(message) {
    var existing = root.querySelector(".quiz-notice");
    if (existing) existing.remove();
    var notice = element("p", "quiz-notice", message);
    root.querySelector(".quiz-actions").before(notice);
  }

  function appendHistory(panel) {
    var history = loadHistory();
    if (!history.length) return;
    var section = element("section", "quiz-history");
    var heading = element("div", "quiz-history-heading");
    heading.append(element("h2", "", "Recent attempts"), button("Clear History", function () {
      if (window.confirm("Clear all saved quiz scores from this browser?")) {
        localStorage.removeItem(STORAGE_KEY);
        renderWelcome();
      }
    }));
    var list = element("div", "quiz-history-list");
    history.slice(0, 5).forEach(function (attempt) {
      var row = element("div", "quiz-history-row");
      row.append(
        element("strong", "", attempt.score + "%"),
        element("span", "", attempt.correct + "/" + attempt.total + " correct"),
        element("time", "", new Date(attempt.date).toLocaleDateString())
      );
      list.appendChild(row);
    });
    section.append(heading, list);
    panel.appendChild(section);
  }

  function saveAttempt(result) {
    var history = loadHistory();
    history.unshift({
      date: new Date().toISOString(),
      score: result.score,
      correct: result.correct,
      total: result.total,
      weakTopics: result.weakTopics.slice()
    });
    try {
      localStorage.setItem(STORAGE_KEY, JSON.stringify(history.slice(0, 20)));
    } catch (error) {
      // Quiz grading still works when browser storage is blocked or full.
    }
  }

  function loadHistory() {
    try {
      var parsed = JSON.parse(localStorage.getItem(STORAGE_KEY) || "[]");
      return Array.isArray(parsed) ? parsed : [];
    } catch (error) {
      return [];
    }
  }

  function button(text, handler) {
    var item = element("button", "win98-button", text);
    item.type = "button";
    item.addEventListener("click", handler);
    return item;
  }

  function element(tag, className, text) {
    var item = document.createElement(tag);
    if (className) item.className = className;
    if (text !== undefined) item.textContent = text;
    return item;
  }
})();
