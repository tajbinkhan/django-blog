from django.apps import apps
from django.conf import settings


class ModelUtility:
	def __init__(self):
		self.__app_configs = apps.get_app_configs()

	def get_model_names(self):
		create_apps = [
			app_label.split(".")[0]
			for app_label in settings.INSTALLED_APPS
			if ".apps" in app_label
		]
		return create_apps

	def get_model_list_with_app_name(self):
		model_list = []
		app_configs = self.__app_configs
		model_names = self.get_model_names()

		try:
			for app_config in app_configs:
				app_models = app_config.get_models()
				if app_config.label in model_names:
					for model in app_models:
						model_list.append((app_config.name, model.__name__))
			return model_list
		except Exception as e:
			print(e)
			return []

	def get_model_list(self):
		model_list = []
		app_configs = self.__app_configs
		model_names = self.get_model_names()

		try:
			for app_config in app_configs:
				app_models = app_config.get_models()
				if app_config.label in model_names:
					for model in app_models:
						model_list.append(model.__name__)
			return model_list
		except Exception as e:
			print(e)
			return []

	def check_the_model_name(self, model_name):
		model_list = self.get_model_list_with_app_name()
		for model in model_list:
			if model[1] == model_name:
				return True
		return False

	def get_model_object(self, model_name):
		try:
			if self.check_the_model_name(model_name):
				model_list = self.get_model_list_with_app_name()
				for model in model_list:
					if model[1] == model_name:
						return apps.get_model(model[0], model[1])
			else:
				return None
		except Exception as e:
			print(e)
			return None
