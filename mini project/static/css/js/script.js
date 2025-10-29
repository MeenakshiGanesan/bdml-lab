// Smooth fade-in animation on page load
document.addEventListener("DOMContentLoaded", () => {
  document.body.style.opacity = 0;
  setTimeout(() => {
    document.body.style.transition = "opacity 0.8s ease-in";
    document.body.style.opacity = 1;
  }, 100);
});

// Typing effect for the heading
const title = document.querySelector("h1");
if (title) {
  const text = title.textContent;
  title.textContent = "";
  let i = 0;
  const typing = setInterval(() => {
    title.textContent += text[i];
    i++;
    if (i === text.length) clearInterval(typing);
  }, 80);
}

// Optional: animate sentiment color in result page
const sentimentText = document.querySelector("h2");
if (sentimentText) {
  sentimentText.style.transition = "transform 0.4s ease, color 0.4s ease";
  sentimentText.addEventListener("mouseover", () => {
    sentimentText.style.transform = "scale(1.1)";
  });
  sentimentText.addEventListener("mouseout", () => {
    sentimentText.style.transform = "scale(1)";
  });
}
