from abc import ABC, abstractmethod


class PhoneBuilder(ABC):

    @abstractmethod
    def set_operation_system(self):
        pass

    @abstractmethod
    def set_processor(self):
        pass

    @abstractmethod
    def set_ram(self):
        pass

    @abstractmethod
    def set_camera(self):
        pass

    @abstractmethod
    def set_display_type(self):
        pass

    @abstractmethod
    def set_screen_resolution(self):
        pass

    @abstractmethod
    def set_screen_size(self):
        pass

    @abstractmethod
    def set_accumulator(self):
        pass

    @abstractmethod
    def set_memory(self):
        pass

    @abstractmethod
    def add_charging_for_the_phone(self):
        pass

    @abstractmethod
    def add_headphones_for_the_phone(self):
        pass

    @abstractmethod
    def add_phone_case(self):
        pass

    @abstractmethod
    def add_protective_glass_for_the_phone(self):
        pass

    @abstractmethod
    def get_package_contents(self):
        pass


class AndroidBuilder(PhoneBuilder):

    def __init__(self):
        self.phone = Phone()

    def set_operation_system(self):
        component = 'Operation System: Android'
        self.phone.update_list_of_phones(component)

    def set_processor(self):
        component = 'Processor: Snapdragon 888'
        self.phone.update_list_of_phones(component)

    def set_ram(self):
        component = 'RAM: 6GB'
        self.phone.update_list_of_phones(component)

    def set_camera(self):
        component = 'Camera: 40mp'
        self.phone.update_list_of_phones(component)

    def set_display_type(self):
        component = 'Display Type: Dynamic AMOLED'
        self.phone.update_list_of_phones(component)

    def set_screen_resolution(self):
        component = 'Screen Resolution: 1125x2436'
        self.phone.update_list_of_phones(component)

    def set_screen_size(self):
        component = 'Screen Size: 5.8-inch'
        self.phone.update_list_of_phones(component)

    def set_accumulator(self):
        component = 'Accumulator: 4500 mAh'
        self.phone.update_list_of_phones(component)

    def set_memory(self):
        component = '1TB'
        self.phone.update_list_of_phones(component)

    def add_charging_for_the_phone(self):
        package = 'Charging: ColorWay 1 USB Quick Charge 3.0'
        self.phone.update_package_contents(package)

    def add_headphones_for_the_phone(self):
        package = 'Headphones: Samsung Galaxy Buds FE SM-R400'
        self.phone.update_package_contents(package)

    def add_phone_case(self):
        package = 'Phone case for Android Phone'
        self.phone.update_package_contents(package)

    def add_protective_glass_for_the_phone(self):
        package = 'Protective glass for Android Phone'
        self.phone.update_package_contents(package)

    def get_package_contents(self):
        return self.phone





class IphoneBuilder(PhoneBuilder):

    def __init__(self):
        self.phone = Phone()

    def set_operation_system(self):
        component = 'Operation System: IOS'
        self.phone.update_list_of_phones(component)

    def set_processor(self):
        component = 'Processor: Apple A17 Pro'
        self.phone.update_list_of_phones(component)

    def set_ram(self):
        component = 'RAM: 8GB'
        self.phone.update_list_of_phones(component)

    def set_camera(self):
        component = 'Camera: 25mp'
        self.phone.update_list_of_phones(component)

    def set_display_type(self):
        component = 'Display Type: Super Retina XDR OLED'
        self.phone.update_list_of_phones(component)

    def set_screen_resolution(self):
        component = 'Screen Resolution: 2796x1290'
        self.phone.update_list_of_phones(component)

    def set_screen_size(self):
        component = 'Screen Size: 6.7-inch'
        self.phone.update_list_of_phones(component)

    def set_accumulator(self):
        component = 'Accumulator: 5000 mAh'
        self.phone.update_list_of_phones(component)

    def set_memory(self):
        component = '512GB'
        self.phone.update_list_of_phones(component)

    def add_charging_for_the_phone(self):
        package = 'Charging: Apple 20W USB-C Power Adapter'
        self.phone.update_package_contents(package)

    def add_headphones_for_the_phone(self):
        package = 'Headphones: Apple AirPods Pro 2nd Gen'
        self.phone.update_package_contents(package)

    def add_phone_case(self):
        package = 'Phone case for Iphone'
        self.phone.update_package_contents(package)

    def add_protective_glass_for_the_phone(self):
        package = 'Protective glass for Iphone'
        self.phone.update_package_contents(package)

    def get_package_contents(self):
        return self.phone


class Phone:

    def __init__(self):
        self.phones = []
        self.package_contents = []

    def update_list_of_phones(self, component):
        self.phones.append(component)

    def update_package_contents(self, package):
        self.package_contents.append(package)

    def __str__(self):
        newline = '\n'
        if len(self.package_contents) == 0:
            contents = 'Only the phone is included in the package'
        else:
            contents = newline.join(self.package_contents)
        return f'Phone characteristics:\n{newline.join(self.phones)}\nPhone package contents:\n{contents}'


class PhoneDirector:

    def only_the_phone_included(self, builder: PhoneBuilder):
        builder.set_operation_system()
        builder.set_processor()
        builder.set_ram()
        builder.set_camera()
        builder.set_display_type()
        builder.set_screen_size()
        builder.set_screen_resolution()
        builder.set_accumulator()
        builder.set_memory()
        return builder.get_package_contents()

    def minimal_phone_package_contents(self, builder: PhoneBuilder):
        self.only_the_phone_included(builder)
        builder.add_charging_for_the_phone()
        builder.add_headphones_for_the_phone()
        return builder.get_package_contents()

    def full_phone_package_contents(self, builder: PhoneBuilder):
        self.only_the_phone_included(builder)
        builder.add_charging_for_the_phone()
        builder.add_headphones_for_the_phone()
        builder.add_phone_case()
        builder.add_protective_glass_for_the_phone()
        return builder.get_package_contents()



first_android = AndroidBuilder()
second_android = AndroidBuilder()
iphone = IphoneBuilder()
phone_director = PhoneDirector()

only_android = phone_director.only_the_phone_included(first_android)
print(only_android)
print()
minimal_package = phone_director.minimal_phone_package_contents(second_android)
print(minimal_package)
print()
full_package = phone_director.full_phone_package_contents(iphone)
print(full_package)



