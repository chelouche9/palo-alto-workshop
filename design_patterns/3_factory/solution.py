class Button:
    def on_click(self):
        pass

class iOSButton(Button):
    def on_click(self):
        print('I am on iOS')

class AndroidButton(Button):
    def on_click(self):
        print('I am on Android')

class ButtonFactory:
    def create_button(self, os: str) -> Button:
        if os == 'ios':
            return iOSButton()
        elif os == 'android':
            return AndroidButton()
        else:
            raise ValueError('Invalid os type')

factory = ButtonFactory()

ios_button = factory.create_button('ios')
ios_button.on_click()

android_button = factory.create_button('android')
android_button.on_click()