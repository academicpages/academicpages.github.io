const firstChoiceButton = document.querySelector('[data-js="choice-button-1"]');
const AnswerButton = document.querySelector('[data-js="active-button"]');
const originalTextElement = firstChoiceButton.querySelector('.item-text-cbox');
const conditionalTextElement = firstChoiceButton.querySelector('.text-conditional');

firstChoiceButton.addEventListener("click", () => {
  firstChoiceButton.classList.toggle("dark");
  AnswerButton.classList.add("dark");
  

  if (!firstChoiceButton.classList.contains("dark")) {
    // Show the conditional text and hide the original text
    originalTextElement.style.display = "none";
    conditionalTextElement.style.display = "block";
    originalTextElement.textContent = originalTextElement.dataset.originalText;
  
    
    AnswerButton.classList.remove("dark");
  } else {
    // Show the original text and hide the conditional text
    originalTextElement.style.display = "block";
    conditionalTextElement.style.display = "none";
    AnswerButton.classList.add("dark");
    
  }
});
