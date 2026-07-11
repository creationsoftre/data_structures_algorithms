(function () {
  "use strict";

  // Question template: duplicate this object and give each question a unique id.
  // Valid competencies are listed in QuizEngine.weights.
  window.QuizQuestions = [
    {
      id: "sample-01",
      competency: "Explains Algorithms",
      topic: "Sample Topic",
      prompt: "Which answer demonstrates the format of a multiple-choice quiz question?",
      choices: [
        "The correct answer",
        "An incorrect distractor",
        "Another incorrect distractor",
        "A final incorrect distractor"
      ],
      answer: 0,
      explanation: "This sample shows the required fields: competency, topic, prompt, four choices, the zero-based answer index, and an explanation."
    }
  ];
})();
