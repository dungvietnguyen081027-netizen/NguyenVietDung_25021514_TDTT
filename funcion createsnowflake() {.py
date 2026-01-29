function createSnowflake() {
    const snow = document.createElement('div');
    snow.classList.add('snowflake');
    snow.textContent = '❄';
    snow.style.left = Math.random() * window.innerWidth + 'px';
    snow.style.animationDuration = (Math.random() * 10 + 15) + 's';
    snow.style.fontSize = (Math.random() * 20 + 10) + 'px';
    document.body.appendChild(snow);
    setTimeout(() => {
        snow.remove();
    }, 25000);
}
setInterval(createSnowflake, 200);