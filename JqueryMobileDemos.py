import sublime, sublime_plugin, webbrowser
from string import Template

settings = None

class JqueryMobileDemos(sublime_plugin.TextCommand):

  def run(self, edit):
    globals()['settings'] = sublime.load_settings('Default.sublime-settings')
    caption = 'Enter demos'
    self.view.window().show_input_panel(
      caption, 
      "",
      self.on_panel_done, 
      None,
      None)

  def on_panel_done(self, user_input):
    path = Template("$version/$demo").safe_substitute(version=settings.get('version'), demo=user_input)
    url = Template("$host/$path").safe_substitute(host=settings.get('host'), path=path)
    self.view.run_command('open_browser', { "url": url })


class OpenBrowserCommand(sublime_plugin.TextCommand):

  def run(self, edit, url):
    webbrowser.open_new(url)