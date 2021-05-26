const btn = document.querySelector('.dkMode');

const currentTheme = localStorage.getItem('theme');
if (currentTheme == 'dark') {
    document.body.classList.add('darkMode');
}

btn.addEventListener('click', function() {
    document.body.classList.toggle('darkMode');
    let theme = 'light';
    if (document.body.classList.contains('darkMode')) {
        theme = 'dark'
    }
    localStorage.setItem('theme', theme);
});
