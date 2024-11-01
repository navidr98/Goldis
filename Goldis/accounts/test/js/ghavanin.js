const karbari = document.getElementById('karbari')
const karbariExplain = document.getElementById('karbariExplain')
const vajh = document.getElementById('vajh')
const vajhExplain = document.getElementById('vajhExplain')
const tahvil = document.getElementById('tahvil')
const tahvilExplain = document.getElementById('tahvilExplain')
const moaref = document.getElementById('moaref')
const moarefExplain = document.getElementById('moarefExplain')
const hedye = document.getElementById('hedye')
const hedyeExplain = document.getElementById('hedyeExplain')

karbari.addEventListener('click', function() {
    if (karbariExplain.style.display === 'none') {
        karbariExplain.style.display = 'block'
        vajhExplain.style.display = 'none'
        tahvilExplain.style.display = 'none'
        moarefExplain.style.display = 'none'
        hedyeExplain.style.display = 'none'
    } else {
        karbariExplain.style.display = 'none'
    }
})
vajh.addEventListener('click', function() {
    if (vajhExplain.style.display === 'none') {
        vajhExplain.style.display = 'block'
        karbariExplain.style.display = 'none'
        tahvilExplain.style.display = 'none'
        moarefExplain.style.display = 'none'
        hedyeExplain.style.display = 'none'
    } else {
        vajhExplain.style.display = 'none'
    }
})
tahvil.addEventListener('click', function() {
    if (tahvilExplain.style.display === 'none') {
        tahvilExplain.style.display = 'block'
        vajhExplain.style.display = 'none'
        karbariExplain.style.display = 'none'
        moarefExplain.style.display = 'none'
        hedyeExplain.style.display = 'none'
    } else {
        tahvilExplain.style.display = 'none'
    }
})
moaref.addEventListener('click', function() {
    if (moarefExplain.style.display === 'none') {
        moarefExplain.style.display = 'block'
        vajhExplain.style.display = 'none'
        tahvilExplain.style.display = 'none'
        karbariExplain.style.display = 'none'
        hedyeExplain.style.display = 'none'
    } else {
        moarefExplain.style.display = 'none'
    }
})
hedye.addEventListener('click', function() {
    if (hedyeExplain.style.display === 'none') {
        hedyeExplain.style.display = 'block'
        vajhExplain.style.display = 'none'
        tahvilExplain.style.display = 'none'
        moarefExplain.style.display = 'none'
        karbariExplain.style.display = 'none'
    } else {
        hedyeExplain.style.display = 'none'
    }
})
