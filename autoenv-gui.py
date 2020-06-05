from kivy.app import App

#Layout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout

#UI Widgets
from kivy.uix.label import Label
from kivy.uix.button import Button

class AutoEnvApp(App):

	def build(self):
		root = BoxLayout(orientation = 'vertical')

		title = Label(text = 'AutoEnv', size_hint_y = 1)

		body = BoxLayout(orientation = 'vertical', size_hint_y = 4, width = root.width*(7/8))

		subtitle = BoxLayout(text = 'My Environments')


		body.add_widget(subtitle)

		root.add_widget(title)
		root.add_widget(body)

		return root


if __name__ == "__main__":
	AutoEnvApp().run()