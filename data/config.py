from pydantic_settings import BaseSettings
import json

class PhrasesClass(BaseSettings):
    class Config:
        extra = "allow"

class ButtonsClass(BaseSettings):
    class Config:
        extra = "allow"

class FSMBaseSettingsClass(BaseSettings):
    class Config:
        extra = "allow"

class FSMAnotherClass(BaseSettings):
    class Config:
        extra = "allow"

with open("phrases.json", encoding="UTF-8") as phrases_file:

    phrases = json.load(phrases_file)

with open("buttons.json", encoding="UTF-8") as buttons_file:
    buttons = json.load(buttons_file)

with open("FSMBase.json", encoding="UTF-8") as fsm_base_file:
    fsm_base = json.load(fsm_base_file)

with open("FSMAnother.json", encoding="UTF-8") as fsm_another_file:
    fsm_another = json.load(fsm_another_file)

Phrases = PhrasesClass(**phrases)
Buttons = ButtonsClass(**buttons)
FSMBaseSettings = FSMBaseSettingsClass(**fsm_base)
FSMAnother = FSMAnotherClass(**fsm_another)
