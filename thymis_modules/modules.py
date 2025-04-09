import thymis_controller
import thymis_controller.lib
import pathlib

from thymis_controller.models import Setting, ModuleSettings
from thymis_controller.modules import Module, LocalizedString


class Language(Module):
    displayName: str = "Home Assistant"

    language = Setting(
        display_name=LocalizedString(
            en="System language",
            de="Systemsprache",
        ),
        type=modules.SelectOneType(select_one=["en_US.UTF-8", "de_DE.UTF-8"]),
        default="en_US.UTF-8",
        description="language setting",
        example="normal",
        order=50,
    )

     def write_nix_settings(
        self,
        f,
        path,
        module_settings: thymis_controller.models.ModuleSettings,
        priority: int,
        project: thymis_controller.project.Project,
    ):
        language = (
            module_settings.settings["language"]
            if "language" in module_settings.settings
            else self.language.default
        )

        f.write(
            f"""
            i18n.defaultLocale = "{language}";
            """
        )
    
