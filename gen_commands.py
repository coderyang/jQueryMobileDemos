import re
import shutil
from pyquery import PyQuery as pq
from StringIO import StringIO
from string import Template

rhref = re.compile(r'href=.*?/(?P<path_name>[^\.]*?)/')

url = "http://demos.jquerymobile.com/1.4.5/"

html = pq(url)

list_item = html('.jqm-list:eq(0) > li')

output = StringIO()


tpl = """
  {
    \"caption\": \"JQM Demo: $path\",
    \"command\": \"open_browser\",
    \"args\": {
      \"url\": \"http://demos.jquerymobile.com/1.4.5/$path/\"
      }
  },"""

for item in list_item:
  item = pq(item)
  collapsible_content = item.find(".ui-collapsible-content")
  has_collapsible_content = collapsible_content.length
  if not has_collapsible_content:
    path_name = rhref.search(item.html().encode('utf-8')).groupdict()['path_name']
    output.write(
      Template(tpl).safe_substitute(path=path_name)
    )
  else:
    collapsible_list_item = collapsible_content.find('li')
    for item in collapsible_list_item:
      item = pq(item)
      path_name = rhref.search(item.html().encode('utf-8')).groupdict()['path_name']
      output.write(
        Template(tpl).safe_substitute(path=path_name)
      )

output.seek(0)
with open('Default.sublime-commands.copy', 'w+') as f:
  shutil.copyfileobj(output, f)