from abc import ABC, abstractmethod
class AbstractMainAppClass(ABC):

    @abstractmethod
    def configure_grid_main(self):
        pass

    @abstractmethod
    def frame_main_creation(self):
        pass

    @abstractmethod
    def progress_bar_creation(self):
        pass

    @abstractmethod
    def start_loading(self):
        pass

    @abstractmethod
    def update_progress(self, value):
        pass

    @abstractmethod
    def bind_creation(self):
        pass