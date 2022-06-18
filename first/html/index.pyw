import webbrowser
import os
  
f = open('GFG.html', 'w')
html_template = """
<html>
<head>
<script>
     let urlPath = 'kasparov.as'
     window.history.pushState({"html":response.html,"pageTitle":response.pageTitle},"", urlPath);

</script>
</head>
<body>
<p>Geeks For Geeks</p>
  
</body>
</html>
"""

f.write(html_template)
  
f.close()
  
# 1st method how to open html files in chrome using
filename = 'file:///'+os.getcwd()+'/' + 'GFG.html'
webbrowser.open_new_tab(filename)