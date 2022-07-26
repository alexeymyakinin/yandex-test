import enum


class CurrencyCode(str, enum.Enum):
    """
    Available currencies enumeration

    RUB - Российский рубль
    EUR - Евро
    USD - Доллар США
    GBP - Фунт стерлингов
    UAH - Украинская гривна
    BYR - Белорусский рубль (не используется с 1 июля 2016)
    BYN - Белорусский рубль
    KZT - Казахский тенге
    AZN - Азербайджанский манат
    CHF - Швейцарский франк
    CZK - Чешская крона
    CAD - Канадский доллар
    PLN - Польский злотый
    SEK - Шведская крона
    TRY - Турецкая лира
    CNY - Китайский юань
    INR - Индийская рупия
    BRL - Бразильский реал
    ZAR - Южноафриканский рэнд
    UZS - Узбекский сум
    BGN - Болгарский лев
    RON - Румынский лей
    AUD - Австралийский доллар
    HKD - Гонконгский доллар
    GEL - Грузинский лари
    KGS - Киргизский сом
    AMD - Армянский драм
    AED - Дирхам ОАЭ
    """

    RUB = "RUB"
    EUR = "EUR"
    USD = "USD"
    GBP = "GBP"
    UAH = "UAH"
    BYR = "BYR"
    BYN = "BYN"
    KZT = "KZT"
    AZN = "AZN"
    CHF = "CHF"
    CZK = "CZK"
    CAD = "CAD"
    PLN = "PLN"
    SEK = "SEK"
    TRY = "TRY"
    CNY = "CNY"
    INR = "INR"
    BRL = "BRL"
    ZAR = "ZAR"
    UZS = "UZS"
    BGN = "BGN"
    RON = "RON"
    AUD = "AUD"
    HKD = "HKD"
    GEL = "GEL"
    KGS = "KGS"
    AMD = "AMD"
    AED = "AED"
