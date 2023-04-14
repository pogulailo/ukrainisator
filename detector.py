from lingua import Language, LanguageDetectorBuilder, isocode


def get_language_code(text: str) -> isocode.IsoCode639_3 | None:
    languages = [Language.UKRAINIAN, Language.RUSSIAN]
    detector = LanguageDetectorBuilder.from_languages(*languages).build()
    language = detector.detect_language_of(text)

    if not language:
        return

    return language.iso_code_639_3
