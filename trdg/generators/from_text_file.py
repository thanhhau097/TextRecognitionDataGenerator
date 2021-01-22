import os

from .from_strings import GeneratorFromStrings
from ..data_generator import FakeTextDataGenerator
from ..string_generator import create_strings_from_file
from ..utils import load_dict, load_fonts


class GeneratorFromTextFile:
    """Generator that uses sentences taken from random Wikipedia articles"""

    def __init__(
        self,
        folder='',
        count=-1,
        minimum_length=1,
        maximum_length=50,
        fonts=[],
        language="en",
        size=32,
        skewing_angle=0,
        random_skew=False,
        blur=0,
        random_blur=False,
        background_type=0,
        distorsion_type=0,
        distorsion_orientation=0,
        is_handwritten=False,
        width=-1,
        alignment=1,
        text_color="#282828",
        orientation=0,
        space_width=1.0,
        margins=(5, 5, 5, 5),
        fit=False,
    ):
        self.count = count
        self.minimum_length = minimum_length
        self.maximum_length = maximum_length
        self.language = language
        self.files = [os.path.join(folder, f) for f in os.listdir(folder)]
        self.index = 0
        self.generator = GeneratorFromStrings(
            create_strings_from_file(self.files[self.index], maximum_length),
            count=count,
            fonts=fonts if len(fonts) else load_fonts(language),
            language=language,
            size=size,
            skewing_angle=skewing_angle,
            random_skew=random_skew,
            blur=blur,
            random_blur=random_blur,
            background_type=background_type,
            distorsion_type=distorsion_type,
            distorsion_orientation=distorsion_orientation,
            is_handwritten=is_handwritten,
            width=width,
            alignment=alignment,
            text_color=text_color,
            orientation=orientation,
            space_width=space_width,
            margins=margins,
            fit=fit,
        )

    def __iter__(self):
        return self

    def __next__(self):
        element = None
        while not element:
            try:
                element = self.next()
            except:
                element = None

        return element

    def next(self):
        if self.generator.generated_count >= len(self.generator.strings):
            self.index = (self.index + 1) % len(self.files)
            self.generator.strings = create_strings_from_file(self.files[self.index], maximum_length=self.maximum_length)
            self.generator.generated_count = 0
        return self.generator.next()