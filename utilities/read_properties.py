import yaml

class Read_Config:

    _config_data = None

    @staticmethod
    def lond_config(file_path= "config/config.yaml"):
        if Read_Config._config_data is None:
            with open(file_path, "r", encoding= "utf-8") as file:
                Read_Config._config_data = yaml.safe_load(file)

    @staticmethod
    def get_page_url():
        Read_Config.lond_config()
        return Read_Config._config_data["admin_login_info"]["admin_page_url"]

    @staticmethod
    def get_username():
        Read_Config.lond_config()
        return Read_Config._config_data["admin_login_info"]["username"]

    @staticmethod
    def get_password():
        Read_Config.lond_config()
        return Read_Config._config_data["admin_login_info"]["password"]

    @staticmethod
    def get_password():
        Read_Config.lond_config()
        return Read_Config._config_data["admin_login_info"]["password"]

    @staticmethod
    def get_invalid_username():
        Read_Config.lond_config()
        return Read_Config._config_data["admin_login_info"]["invalid_username"]

    @staticmethod
    def get_locked_username():
        Read_Config.lond_config()
        return Read_Config._config_data["admin_login_info"]["locked_username"]

    @staticmethod
    def get_problem_username():
        Read_Config.lond_config()
        return Read_Config._config_data["admin_login_info"]["problem_username"]

    @staticmethod
    def get_performance_glitch_username():
        Read_Config.lond_config()
        return Read_Config._config_data["admin_login_info"]["performance_glitch_username"]

    @staticmethod
    def get_error_username():
        Read_Config.lond_config()
        return Read_Config._config_data["admin_login_info"]["error_username"]

    @staticmethod
    def get_visual_username():
        Read_Config.lond_config()
        return Read_Config._config_data["admin_login_info"]["visual_username"]