from browser import document
window = document.getElementById('game')

entities = list()
b = document.createElement("div")
b.style.cssText = '''width:56.25%; height:100%; position:absolute; top:50%; left:50%;
transform:translate(-50%, -50%); color:white; background-color:clear;'''
window.appendChild(b)
