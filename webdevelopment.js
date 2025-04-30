let questions = [];

function addQuestion() {
  const question = document.getElementById("question").value;
  const options = [
    document.getElementById("option1").value,
    document.getElementById("option2").value,
    document.getElementById("option3").value,
    document.getElementById("option4").value
  ];
  const correct = parseInt(document.getElementById("correct").value) - 1;

  if (question && options.every(opt => opt) && correct >= 0 && correct < 4) {
    questions.push({ question, options, correct });
    alert("Question added!");
    document.querySelectorAll("input").forEach(input => input.value = "");
  } else {
    alert("Please fill in all fields correctly.");
  }
}

function startQuiz() {
  const quizArea = document.getElementById("quizArea");
  quizArea.innerHTML = "";
  questions.forEach((q, index) => {
    const div = document.createElement("div");
    div.innerHTML = `
      <p><strong>Q${index + 1}:</strong> ${q.question}</p>
      ${q.options.map((opt, i) => `
        <label>
          <input type="radio" name="q${index}" value="${i}"> ${opt}
        </label><br>
      `).join("")}
    `;
    quizArea.appendChild(div);
  });
}

function submitQuiz() {
  let score = 0;
  questions.forEach((q, index) => {
    const selected = document.querySelector(`input[name="q${index}"]:checked`);
    if (selected && parseInt(selected.value) === q.correct) {
      score++;
    }
  });
  document.getElementById("result").innerHTML = `
    <h3>Your Score: ${score}/${questions.length}</h3>
  `;
}
