## Импорт и экспорт XML: Теги и их атрибуты

В таблицах приведены используемые при импорте и экспорте теги, перечислены их атрибуты, дана дополнительная информация. Типы данных, указанные в колонке "Тип", имеют следующее значение:

Булево (истина/ложь)

"0" или " " означает "Нет", "Ложь" или "Выключено". "1" означает "Да", "Истина" или "Включено".

Целое / "Длинное" целое

!!! example "Пример:"

    "", "0", "1", "2" или "-5"

"" равносильно нулю ("0").

Для атрибутов и списков выбора допускается использование только определенных значений, полученных из базы данных изделий. Обзор доступных значений приводится в [соответствующем разделе](xmlexport_o_sellists.md).

Число с плавающей точкой

Разделитель разрядов — точка.

!!! example "Пример:"

    "1.99" или "2.5"

"" равносильно нулю ("0").

Текст

!!! example "Пример:"

    "Это текст" или ''.

Многоязычный текст

Начало и конец многоязычного текста определяется идентификатором языка и точкой с запятой соответственно. Между идентификатором языка и текстом должен стоять символ "@".

!!! example "Пример:"

    de_DE@Schütz; en_US@Contactor;nl_NL@Relais;

###  <partsmanagement>

№ |  Атрибут |  Тип |  Свойство |  Примечание  
---|---|---|---|---  
1 |  count | Long | Число изделий |   
2 |  length-unit | Текст | Единица измерения длины | Вставка значения длины, к примеру "mm" (в мм) или "inch" (в дюймах). Опционально, по умолчанию "мм".  
3 |  weight-unit | Текст | Единица измерения веса |   
4 |  type | Текст | Тип | Тип базы данных изделий. На данный момент применяется только одно значение - "Eplan.PartsManagement". Опциональн.  
5 |  build | Текст | Номер сборки | Номер сборки на момент экспорта. Опциональн.  
6 |  version | Текст | Номер сборки программы |   

### Свойства изделия <part> / <variantx>

!!! note "Замечание:"

Пример:

P_ARTICLE_GROUPSYMBOLMACRO   
Пример: "C:\macro.ema" или "$(MD_MACROS)\Macro.ema"

P_ARTICLE_ECABINET_MACRO   
Пример: "C:\texture.jpg" или "$(MD_IMAGES)\texture.jpg"

**№** | **Атрибут** | **Тип** | **Группа** | **Единица измерения** | **Свойство**  
---|---|---|---|---|---  
1 |  P_ARTICLE_SEALING | Текст (многоязычный) |  |  | Уплотнение  
2 |  P_ARTICLE_STRIPPING_LENGTH | Текст (значение с единицей измерения) | Длина | мм | Длина оболочки (кабель)  
3 |  P_ARTICLE_BOTTOMPANELDISTANCE | Double |  |  | Расстояние до пола  
4 |  P_ARTICLE_TOPPANELDISTANCE | Double |  |  | Расстояние до крыши  
5 |  P_ARTICLE_REARPANELDISTANCE | Double |  |  | Расстояние до задней стенки  
6 |  P_ARTICLE_SIDEPANELDISTANCE | Double |  |  | Расстояние до боковой стенки  
7 |  P_ARTICLE_PROFILEDISTANCE | Double |  |  | Интерв. при постр. в линию  
8 |  P_ARTICLE_DISTANCE_WIRE_HOLD_BACK_NOSE | Double |  |  | Интервал до утолщения  
9 |  P_ARTICLE_OUTPUT_SPEED_MAX | Текст (значение с единицей измерения) | Частота вращения | /min | Частота вращения выходного вала, макс.  
10 |  P_ARTICLE_OUTPUT_SPEED_MIN | Текст (значение с единицей измерения) | Частота вращения | /min | Частота вращения выходного вала, мин.  
11 |  P_ARTICLE_TYPE_OF_MOUNTING | Long |  |  | Тип монтажа  
12 |  P_ARTICLE_STARTING_CURRENT_A | Текст (значение с единицей измерения) | Сила электрического тока | A | Пусковой ток, макс.  
13 |  P_ARTICLE_RUN_UP_TIME | Текст (значение с единицей измерения) | Время | s | Время пуска  
14 |  P_PART_ADDRESS_TITLE | Текст |  |  | Обращение  
15 |  P_ARTICLE_INTAKE_PRESSURE | Текст (значение с единицей измерения) | Давление | бар | Давление всасывания  
16 |  P_ARTICLE_INTAKE_PRESSURE_MAX | Текст (значение с единицей измерения) | Давление | бар | Давление всасывания, макс.  
17 |  P_ARTICLE_INTAKE_PRESSURE_MIN | Текст (значение с единицей измерения) | Давление | бар | Давление всасывания, мин.  
18 |  P_ARTICLE_INTAKE_TEMPERATURE | Текст (значение с единицей измерения) | Температура | °C | Температура всасывания  
19 |  P_ARTICLE_INTAKE_CAPACITY | Текст (значение с единицей измерения) | Объемный поток | л/мин | Всасывающая способность  
20 |  P_ARTICLE_INTAKE_VOLUME | Текст (значение с единицей измерения) | Объемный поток | л/мин | Всасываемый объем  
21 |  P_ARTICLE_SUCTION_VOLUME_FLOW_MAX | Текст (значение с единицей измерения) | Объемный поток | m³/h | Всасываемый объемный поток, макс.  
22 |  P_ARTICLE_INTAKE_VOLUME_FLOW_MIN | Текст (значение с единицей измерения) | Объемный поток | m³/h | Всасываемый объемный поток, мин.  
23 |  P_ARTICLE_START_UP_TIME | Текст (значение с единицей измерения) | Время | s | Время включения  
24 |  P_ARTICLE_CONNECTABLE_CABLE_TYPE | Текст (многоязычный) |  |  | Подключаемый тип кабеля  
25 |  P_ARTICLE_CONNECTION_TYPE | Текст (многоязычный) |  |  | Тип вывода устройства  
26 |  P_PART_TERMINAL_TYPEOFTERMINAL_DEFAULT | Long (список выбора) |  |  | Категория соединения (стандарт)  
27 |  P_ARTICLE_REF_TERMINAL_NAME | Текст |  |  | Схема соединений  
28 |  P_ARTICLE_REF_TERMINAL_OFFSET_X | Double |  |  | Схема соединений: Смещение в направлении Х  
29 |  P_ARTICLE_REF_TERMINAL_OFFSET_Y | Double |  |  | Схема соединений: Смещение в направлении Y  
30 |  P_ARTICLE_APPLICATION_RANGE_OF_THE_CONNECTION_CABLE | Текст (многоязычный) |  |  | Кабель вывода устройства: Область применения  
31 |  P_ARTICLE_CONNECTION_CABLE_COLOUR | Текст (многоязычный) |  |  | Кабель вывода устройства: Цвет  
32 |  P_ARTICLE_CONNECTION_CABLE_LENGTH | Текст (значение с единицей измерения) | Длина | м | Кабель вывода устройства: Длина  
33 |  P_ARTICLE_CROSS_SECTION_OF_THE_CONNECTION_CABLE | Текст (значение с единицей измерения) | Площадь | мм² | Направление вывода устройства: Поперечное сечение  
34 |  P_PART_TERMINAL_TERMINALSIZE_DEFAULT | Текст (значение с единицей измерения) |  |  | Размер присоединения (стандарт)  
35 |  P_ARTICLE_DRIVE_TORQUE | Текст (значение с единицей измерения) | Работа | Н∙м | Вращающий момент привода  
36 |  P_ARTICLE_SPECIFIED_MAXIMUM_DRIVE_TORQUE | Текст (значение с единицей измерения) | Работа | Н∙м | Вращающий момент привода (указанный), макс.  
37 |  P_ARTICLE_SPECIFIED_MINIMUM_DRIVE_TORQUE | Текст (значение с единицей измерения) | Работа | Н∙м | Вращающий момент привода (указанный), мин.  
38 |  P_ARTICLE_NUMBER_OF_TYPES_OF_FIXING_POINTS | Текст (значение с единицей измерения) | Количество | Stück | Количество типов точек крепления  
39 |  P_ARTICLE_NUMBER_OF_OUTPUTS | Long |  |  | Количество выходов  
40 |  P_ARTICLE_NUMBER_OF_FIXING_POINTS | Текст (значение с единицей измерения) | Количество | Stück | Количество точек крепления  
41 |  P_ARTICLE_NUMBER_OF_INPUTS | Long |  |  | Количество входов  
42 |  P_ARTICLE_NUMBER_OF_AUXILIARY_POWER_SPEC_PNEUMATIC | Long |  |  | Количество вспомогательных источников энергии (в частности, пневматических)  
43 |  P_ARTICLE_NUMBER_OF_PROCESS_CONNECTIONS | Long |  |  | Количество точек подключения процесса  
44 |  P_ARTICLE_NUMBER_OF_CONNECTABLE_VALVES | Long |  |  | Количество подключаемых клапанов  
45 |  P_ARTICLE_NUMBER_OF_IPCF_CAPABLE_WIRELESS_MODULES | Текст (значение с единицей измерения) | Количество | Stück | Количество радиомодулей с поддержкой iPCF  
46 |  P_ARTICLE_NUMBER_OF_PNEUMATIC_CONNECTION | Long |  |  | Количество пневматических выводов устройства  
47 |  P_ARTICLE_NUMBER_OF_PNEUMATIC_CONNECTIONS_OUTPUT | Long |  |  | Количество пневматических выводов устройства (выходы)  
48 |  P_ARTICLE_NUMBER_OF_PNEUMATIC_CONNECTIONS_INPUT | Long |  |  | Количество пневматических выводов устройства (входы)  
49 |  P_ARTICLE_NUMBER_OF_PNEUMATIC_CONNECTIONS_EXHAUST | Long |  |  | Количество пневматических выводов устройства (выхлоп)  
50 |  P_ARTICLE_NUMBER_OF_PNEUMATIC_CONNECTIONS_CONTROL_CONNECTION | Long |  |  | Количество пневматических выводов устройства (управляющие выводы устройства)  
51 |  P_ARTICLE_TIGHTENING_TORQUE_ | Текст (значение с единицей измерения) | Работа | Н∙м | Момент затяжки  
52 |  P_ARTICLE_TIGHTENING_TORQUE_MAX | Текст (значение с единицей измерения) | Работа | Н∙м | Момент затяжки, макс.  
53 |  P_ARTICLE_TIGHTENING_TORQUE_MIN | Текст (значение с единицей измерения) | Работа | Н∙м | Момент затяжки, мин.  
54 |  P_ARTICLE_TYPE_OF_SEALING | Текст (многоязычный) |  |  | Тип уплотнения  
55 |  P_ARTICLE_TYPE_OF_SEAL_EX | Текст (многоязычный) |  |  | Тип уплотнения (Ex)  
56 |  P_ARTICLE_TYPE_OF_HEATING_COOLING | Текст (многоязычный) |  |  | Тип отопления / охлаждения  
57 |  P_ARTICLE_COOLING_TYPE | Текст (многоязычный) |  |  | Тип охлаждения  
58 |  P_ARTICLE_TYPE_OF_CONTROL | Текст (многоязычный) |  |  | Тип управления  
59 |  P_ARTICLE_TYPE_OF_CONTROL_COMMAND_TRANSMISSION | Текст (многоязычный) |  |  | Тип управления (передача команд)  
60 |  P_ARTICLE_TYPE_OF_CONTROL_TECHNOLOGY | Текст (многоязычный) |  |  | Тип управления (технология)  
61 |  P_ARTICLE_TYPE_OF_FIXING_POINT | Текст (многоязычный) |  |  | Тип точки крепления  
62 |  P_ARTICLE_TYPE_OF_FLOW | Текст (значение с единицей измерения) | Объемный поток | л/мин | Тип расхода  
63 |  P_ARTICLE_TYPE_OF_COOLING_MEDIUM | Текст (многоязычный) |  |  | Тип хладагента  
64 |  P_ARTICLE_TYPE_OF_SENSOR | Текст (многоязычный) |  |  | Тип датчика  
65 |  P_ARTICLE_TYPE_OF_CERTIFICATE | Текст (многоязычный) |  |  | Тип сертификата  
66 |  P_ARTICLE_DOES_NOT_NEED_3D_MACRO | Булево (истина/ложь) |  |  | Для изделия не требуется 3D-макрос  
67 |  P_ARTICLE_DOES_NOT_NEED_CPP | Булево (истина/ложь) |  |  | Для изделия не требуется схема соединений  
68 |  P_ARTICLE_DOES_NOT_NEED_DRILL | Булево (истина/ложь) |  |  | Для изделия не требуется схема сверления  
69 |  P_ARTICLE_IS_ACCESSORY | Булево (истина/ложь) |  |  | Изделие относится к принадлежностям  
70 |  P_ARTICLE_DESCR1 | Текст (многоязычный) |  |  | Изделие: Обозначение 1  
71 |  P_ARTICLE_DESCR2 | Текст (многоязычный) |  |  | Изделие: Обозначение 2  
72 |  P_ARTICLE_DESCR3 | Текст (многоязычный) |  |  | Изделие: Обозначение 3  
73 |  P_ARTICLE_PARTNR | Текст |  |  | Номер изделия  
74 |  P_ARTICLE_VARIANT_DESCRIPTION | Текст (многоязычный) |  |  | Описание варианта изделия  
75 |  P_ARTICLE_COLLECTION_VOLUME | Текст (значение с единицей измерения) | Объем | л | Объем сбора  
76 |  P_ARTICLE_SNAPHEIGHT | Double |  |  | Высота крепления зажимом  
77 |  P_ARTICLE_ABSORPTION_VOLUME | Текст (значение с единицей измерения) | Объем | л | Объем потребления  
78 |  P_ARTICLE_CAN_BE_LINED_UP | Булево (истина/ложь) |  |  | Последовательный  
79 |  P_ARTICLE_DESIGN_AS_OUTDOOR_CABLE | Текст (многоязычный) |  |  | Исполнение в виде кабеля для наружной прокладки  
80 |  P_ARTICLE_VERSION_AS_MAINTENANCE_REPAIR_SWITCH | Булево (истина/ложь) |  |  | Исполнение в виде переключателя для технического обслуживания / ремонта  
81 |  P_ARTICLE_SURFACE | Long |  |  | Исполнение поверхности  
82 |  P_ARTICLE_DESIGN_OF_THE_FIXING_POINT | Текст (многоязычный) |  |  | Исполнение точки крепления  
83 |  P_ARTICLE_DISCONTINUED | Булево (истина/ложь) |  |  | Деталь, снятая с производства  
84 |  P_ARTICLE_DESIGN_TEMPERATURE | Текст (значение с единицей измерения) | Температура | °C | Расчетная температура  
85 |  P_ARTICLE_BACNET | Текст (многоязычный) |  |  | BACnet  
86 |  P_ARTICLE_NUMBER_OF_HW_INTERFACES_BACNET | Long |  |  | BACnet: Количество аппаратных интерфейсов  
87 |  P_ARTICLE_NUMBER_OF_BACNET_I_O_OBJECTS | Long |  |  | BACnet: Количество объектов ввода/вывода  
88 |  P_ARTICLE_SERVICE_ACCORDING_TO_BACNET_SPECIFICATION | Текст (многоязычный) |  |  | BACnet: Сервис в соответствии со спецификацией BACnet  
89 |  P_ARTICLE_DEVICE_PROFILE_ACCORDING_TO_BACNET_SPECIFICATION | Текст (многоязычный) |  |  | BACnet: Профиль устройств в соответствии со спецификацией BACnet  
90 |  P_ARTICLE_TOTAL_NUMBER_OF_BACNET_OBJECTS | Long |  |  | BACnet: Общее количество объектов  
91 |  P_ARTICLE_STANDARD_BACNET_ | Текст (многоязычный) |  |  | BACnet: Стандарт  
92 |  P_ARTICLE_PRODUCT_FUNCTION_WITH_BACNET | Текст (многоязычный) |  |  | BACnet: Функция продукта  
93 |  P_ARTICLE_PROTOCOL_BACNET | Текст (многоязычный) |  |  | BACnet: Протокол  
94 |  P_ARTICLE_CHARACTER_SET_ACCORDING_TO_BACNET_SPECIFICATION | Текст (многоязычный) |  |  | BACnet: Набор символов в соответствии со спецификацией BACnet  
95 |  P_ARTICLE_TYPE_OF_CONSTRUCTION | Текст (многоязычный) |  |  | Конструкция  
96 |  P_ARTICLE_ENCLOSURE_DESIGN | Текст (многоязычный) |  |  | Конструкция  
97 |  P_ARTICLE_TYPE_OF_DYNAMIC_SEAL | Текст (многоязычный) |  |  | Тип конструкции: Динамическое уплотнение  
98 |  P_ARTICLE_DESIGN_OF_THE_HOUSING | Текст (многоязычный) |  |  | Тип конструкции: Корпус  
99 |  P_ARTICLE_UNIT_DESIGN | Текст (многоязычный) |  |  | Тип конструкции: Устройство  
100 |  P_ARTICLE_DESIGN_OF_THE_TRANSDUCER | Текст (многоязычный) |  |  | Тип конструкции: Измерительный преобразователь  
101 |  P_ARTICLE_DESIGN_OF_THE_SENSOR | Текст (многоязычный) |  |  | Тип конструкции: Датчик  
102 |  P_ARTICLE_TYPE_OF_STATIC_SEAL | Текст (многоязычный) |  |  | Тип конструкции: Статическое уплотнение  
103 |  P_ARTICLE_DISASSEMBLE_SELECTION | Булево (истина/ложь) |  |  | Разбить узел для выбора изделия  
104 |  P_ARTICLE_STRESS | Текст |  |  | Нагрузка  
105 |  P_ARTICLE_PROVISION_OF_THE_CABLE_GLAND | Текст (многоязычный) |  |  | Обеспечение резьбовым соединением кабеля  
106 |  P_ARTICLE_PROVISION_OF_THE_CABLE | Текст (многоязычный) |  |  | Обеспечение кабелем  
107 |  P_ARTICLE_LOAD_CAPACITY | Текст (значение с единицей измерения) | Сила электрического тока | A | Нагрузочная способность кабеля  
108 |  P_ARTICLE_ULTIMATE_BREAKING_CAPACITY_AC | Текст (значение с единицей измерения) | Сила электрического тока | A | Номинальная отключающая способность (при переменном токе)  
109 |  P_ARTICLE_ULTIMATE_BREAKING_CAPACITY_DC | Текст (значение с единицей измерения) | Сила электрического тока | A | Номинальная отключающая способность (при постоянном токе)  
110 |  P_ARTICLE_ULTIMATE_BREAKING_CAPACITY | Текст (значение с единицей измерения) | Сила электрического тока | A | Номинальная граничная наибольшая отключающая способность при коротком замыкании (Icu)  
111 |  P_ARTICLE_MAKING_CAPACITY | Текст (значение с единицей измерения) | Сила электрического тока | A | Номинальная граничная наибольшая включающая способность при коротком замыкании (Icm)  
112 |  P_ARTICLE_RATED_APPARENT_POWER | Текст (значение с единицей измерения) | Мощность | V*A | Номинальная полная мощность  
113 |  P_ARTICLE_RATED_CURRENT_IN_FOR_THE_POWER_LOSS_SPECIFICATION | Текст (значение с единицей измерения) | Сила электрического тока | A | Номинальный ток (In) для указания мощности потерь  
114 |  P_ARTICLE_FREE_DATA_IDENTNAME_#index | Текст |  |  | Определенные пользователем свойства: Идентифицирующее имя  
115 |  P_ARTICLE_FREE_DATA_NEWVALUE_#index | Текст (многоязычный) |  |  | Определенные пользователем свойства: Значение  
116 |  P_ARTICLE_USAGE | Текст |  |  | Приобретение  
117 |  P_ARTICLE_NOTE | Текст (многоязычный) |  |  | Описание  
118 |  P_PART_ADDRESS_NOTE | Текст (многоязычный) |  |  | Описание (адрес)  
119 |  P_PART_TERMINAL_DESCRIPTION | Текст (многоязычный) |  |  | Описание (схема соединений)  
120 |  P_PART_CONSTRUCTION_DESCRIPTION | Текст (многоязычный) |  |  | Описание (схема сверления)  
121 |  P_PART_ACCESSORYLIST_DESCRIPTION | Текст (многоязычный) |  |  | Описание (список принадлежностей)  
122 |  P_PART_ACCESSORYPLACEMENT_DESCRIPTION | Текст (многоязычный) |  |  | Описание (размещение принадлежностей)  
123 |  P_ARTICLE_ORDERNR | Текст |  |  | Номер для заказа  
124 |  P_ARTICLE_SERVICE_BREAKING_CAPACITY_PERCENT | Текст (значение с единицей измерения) | Процент | % | Эксплуатационная наибольшая отключающая способность при коротком замыкании (Ics в % от Icu)  
125 |  P_ARTICLE_SERVICE_BREAKING_CAPACITY | Текст (значение с единицей измерения) | Сила электрического тока | A | Эксплуатационная наибольшая отключающая способность при коротком замыкании (Ics)  
126 |  P_ARTICLE_OPERATING_VOLTAGE_WITH_AC_50_HZ_MAX | Текст (значение с единицей измерения) | Электрическое напряжение | V | Рабочее напряжение (при переменном токе 50 Гц), макс.  
127 |  P_ARTICLE_OPERATING_VOLTAGE_WITH_AC_50_HZ_MIN | Текст (значение с единицей измерения) | Электрическое напряжение | V | Рабочее напряжение (при переменном токе 50 Гц), мин.  
128 |  P_ARTICLE_OPERATING_VOLTAGE_WITH_AC_60_HZ_MAX | Текст (значение с единицей измерения) | Электрическое напряжение | V | Рабочее напряжение (при переменном токе 60 Гц), макс.  
129 |  P_ARTICLE_OPERATING_VOLTAGE_WITH_AC_60_HZ_MIN | Текст (значение с единицей измерения) | Электрическое напряжение | V | Рабочее напряжение (при переменном токе 60 Гц), мин.  
130 |  P_ARTICLE_OPERATING_VOLTAGE_WITH_DC_MAX | Текст (значение с единицей измерения) | Электрическое напряжение | V | Рабочее напряжение (при постоянном токе), макс.  
131 |  P_ARTICLE_OPERATING_VOLTAGE_WITH_DC_MIN | Текст (значение с единицей измерения) | Электрическое напряжение | V | Рабочее напряжение (при постоянном токе), мин.  
132 |  P_ARTICLE_OPERATING_TEMPERATURE | Текст (значение с единицей измерения) | Температура | °C | Рабочая температура  
133 |  P_ARTICLE_OPERATING_TEMPERATURE_MAX | Текст (значение с единицей измерения) | Температура | °C | Рабочая температура, макс.  
134 |  P_ARTICLE_OPERATING_TEMPERATURE_MIN | Текст (значение с единицей измерения) | Температура | °C | Рабочая температура, мин.  
135 |  P_ARTICLE_ACCURACY_FOR_OPERATING_VOLUME_FLOW_RATE | Текст (значение с единицей измерения) | Объемный поток | m³/s | Рабочий объемный расход: Точность  
136 |  P_ARTICLE_TYPE_OF_OPERATION | Текст (многоязычный) |  |  | Тип приведения в действие  
137 |  P_ARTICLE_DESIGNATION_OF_THE_MEASURING_METHOD | Текст (многоязычный) |  |  | Обозначение метода измерения  
138 |  P_ARTICLE_PICTUREFILE | Текст |  |  | Графический файл  
139 |  P_ARTICLE_DISASSEMBLE_SELECTIONLEVEL | Long |  |  | До степени  
140 |  P_ARTICLE_REF_CONSTRUCTION_NAME | Текст |  |  | Схема сверления  
141 |  P_ARTICLE_FIRE_PROTECTION_PROPERTIES | Текст (многоязычный) |  |  | Противопожарные свойства  
142 |  P_ARTICLE_WIDTH | Double |  |  | Ширина  
143 |  P_ARTICLE_VPROFILEWIDTH | Double |  |  | Ширина профиля, вертик.  
144 |  P_ARTICLE_WIDTHTOP | Double |  |  | Ширина вверху  
145 |  P_ARTICLE_WIDTHBOTTOM | Double |  |  | Ширина внизу  
146 |  P_ARTICLE_BUNDLE_MAXDIAMETER | Double |  |  | Максимальный диаметр жгута  
147 |  P_ARTICLE_BUNDLE_MINDIAMETER | Double |  |  | Минимальный диаметр жгута  
148 |  P_ARTICLE_CO2_EMISSION | Текст (значение с единицей измерения) | Выброс | g/kWh | Выброс CO2  
149 |  P_ARTICLE_EDP_IMPORT_DATE | Целое число (время) |  |  | Дата импорта Data Portal  
150 |  P_ARTICLE_PARTTYPE | Long |  |  | Тип записи данных  
151 |  P_ARTICLE_CONTINUOUS_HEAT_PERFORMANCE_AT_10_C | Текст (значение с единицей измерения) | Мощность | Вт | Постоянная теплопроизводительность (при 10 °C)  
152 |  P_ARTICLE_CONTINUOUS_HEAT_PERFORMANCE_AT_20_C | Текст (значение с единицей измерения) | Мощность | Вт | Постоянная теплопроизводительность (при 20 °C)  
153 |  P_ARTICLE_DENSITY | Текст (значение с единицей измерения) | Масса на объем | kg/m³ | Плотность  
154 |  P_ARTICLE_THICKNESS_OF_MATERIAL | Текст (значение с единицей измерения) | Длина | мм | Толщина материала  
155 |  P_ARTICLE_TORQUE_ | Текст (значение с единицей измерения) | Работа | Н∙м | Вращающий момент  
156 |  P_ARTICLE_TORQUE_AT_MAX_SPEED | Текст (значение с единицей измерения) | Работа | Н∙м | Вращающий момент (при максимальной частоте вращения)  
157 |  P_ARTICLE_TORQUE_AT_MIN_SPEED | Текст (значение с единицей измерения) | Работа | Н∙м | Вращающий момент (при минимальной частоте вращения)  
158 |  P_ARTICLE_TORQUE_MAX_ | Текст (значение с единицей измерения) | Работа | Н∙м | Вращающий момент, макс.  
159 |  P_ARTICLE_SPEED_MAX | Текст (значение с единицей измерения) | Частота | Гц | Частота вращения, макс.  
160 |  P_ARTICLE_SPEED_MIN | Текст (значение с единицей измерения) | Частота | Гц | Частота вращения, мин.  
161 |  P_ARTICLE_NOMINAL_PRESSURE_RANGE | Текст (значение с единицей измерения) |  |  | Диапазон печати  
162 |  P_ARTICLE_DIMENSIONS_OF_THE_PRESSURED_AREA | Текст (значение с единицей измерения) | Площадь | мм² | Площадь давления: Размеры  
163 |  P_ARTICLE_PRESSURE_STAGE | Текст (значение с единицей измерения) | Давление | бар | Ступень давления  
164 |  P_ARTICLE_SECONDARY_CASING_PRESSURE_STAGE | Текст (значение с единицей измерения) | Давление | бар | Ступень давления вторичного корпуса  
165 |  P_ARTICLE_FLOW_RATE_OPERATING_NORMAL_VOLUME_FLOW | Текст (значение с единицей измерения) | Объемный поток | m³/s | Расход (рабочий / стандартный объемный расход)  
166 |  P_ARTICLE_FLOW_RATE | Текст (значение с единицей измерения) | Объемный поток | m³/s | Интенсивность расхода  
167 |  P_ARTICLE_FLOW_DIRECTION | Текст (многоязычный) |  |  | Направление потока: Рабочее направление потока  
168 |  P_ARTICLE_DIAMETER_OF_THE_CABLE_ENTRY | Текст (значение с единицей измерения) | Площадь | мм² | Диаметр: Кабельный ввод  
169 |  P_ARTICLE_THROUGHPUT | Текст (значение с единицей измерения) | Объемный поток | m³/h | Производительность  
170 |  P_ARTICLE_ACCURACY_FOR_DYNAMIC_VISCOSITY | Текст (значение с единицей измерения) | Динамическая вязкость | kg/m*s | Динамическая вязкость: Точность  
171 |  P_ARTICLE_INITIAL_VALUE_OF_THE_DYNAMIC_VISCOSITY_RANGE | Текст (значение с единицей измерения) | Динамическая вязкость | kg/m*s | Диапазон динамической вязкости: Начальное значение  
172 |  P_ARTICLE_END_VALUE_OF_THE_DYNAMIC_VISCOSITY_RANGE | Текст (значение с единицей измерения) | Динамическая вязкость | kg/m*s | Диапазон динамической вязкости: Конечное значение  
173 |  P_PART_ADDRESS_EMAIL | Текст |  |  | Электронная почта  
174 |  P_ARTICLE_EMC_DESIGN_PRESENT | Булево (истина/ложь) |  |  | Доступно исполнение для ЭМС  
175 |  P_ARTICLE_ERPNR | Текст |  |  | Номер ERP / PDM 1  
176 |  P_ARTICLE_ERPNR_DESCRIPTION | Текст (многоязычный) |  |  | Номер ERP / PDM 1: Описание  
177 |  P_ARTICLE_ERPNR_2 | Текст |  |  | Номер ERP / PDM 2  
178 |  P_ARTICLE_ERPNR_DESCRIPTION_2 | Текст (многоязычный) |  |  | Номер ERP / PDM 2: Описание  
179 |  P_ARTICLE_ERPNR_3 | Текст |  |  | Номер ERP / PDM 3  
180 |  P_ARTICLE_ERPNR_DESCRIPTION_3 | Текст (многоязычный) |  |  | Номер ERP / PDM 3: Описание  
181 |  P_ARTICLE_ERPNR_4 | Текст |  |  | Номер ERP / PDM 4  
182 |  P_ARTICLE_ERPNR_DESCRIPTION_4 | Текст (многоязычный) |  |  | Номер ERP / PDM 4: Описание  
183 |  P_ARTICLE_ERPNR_5 | Текст |  |  | Номер ERP / PDM 5  
184 |  P_ARTICLE_ERPNR_DESCRIPTION_5 | Текст (многоязычный) |  |  | Номер ERP / PDM 5: Описание  
185 |  P_ARTICLE_ERPNR_6 | Текст |  |  | Номер ERP / PDM 6  
186 |  P_ARTICLE_ERPNR_DESCRIPTION_6 | Текст (многоязычный) |  |  | Номер ERP / PDM 6: Описание  
187 |  P_ARTICLE_ERPNR_7 | Текст |  |  | Номер ERP / PDM 7  
188 |  P_ARTICLE_ERPNR_DESCRIPTION_7 | Текст (многоязычный) |  |  | Номер ERP / PDM 7: Описание  
189 |  P_ARTICLE_ERPNR_8 | Текст |  |  | Номер ERP / PDM 8  
190 |  P_ARTICLE_ERPNR_DESCRIPTION_8 | Текст (многоязычный) |  |  | Номер ERP / PDM 8: Описание  
191 |  P_ARTICLE_ERPNR_9 | Текст |  |  | Номер ERP / PDM 9  
192 |  P_ARTICLE_ERPNR_DESCRIPTION_9 | Текст (многоязычный) |  |  | Номер ERP / PDM 9: Описание  
193 |  P_ARTICLE_ERPNR_10 | Текст |  |  | Номер ERP / PDM 10  
194 |  P_ARTICLE_ERPNR_DESCRIPTION_10 | Текст (многоязычный) |  |  | Номер ERP / PDM 10: Описание  
195 |  P_ARTICLE_EFFECTIVE_DELIVERY_RATE | Текст (значение с единицей измерения) | Количество | Stück | Эффективная величина подачи  
196 |  P_ARTICLE_CALIBRATION_AUTHORISATION | Текст (многоязычный) |  |  | Метрологический допуск  
197 |  P_ARTICLE_SPACING_LEFT | Double |  |  | Интервал установки, ширина слева  
198 |  P_ARTICLE_SPACING_RIGHT | Double |  |  | Интервал установки, ширина справа  
199 |  P_ARTICLE_SPACING_ABOVE | Double |  |  | Интервал установки, высота вверху  
200 |  P_ARTICLE_SPACING_BELOW | Double |  |  | Интервал установки, высота внизу  
201 |  P_ARTICLE_SPACING_REAR | Double |  |  | Интервал устан., глубина сзади  
202 |  P_ARTICLE_SPACING_FRONT | Double |  |  | Интервал устан., глубина спереди  
203 |  P_ARTICLE_MOUNTING_FORM | Текст (многоязычный) |  |  | Форма установки  
204 |  P_ARTICLE_INSTALLATION_POSITION | Текст (многоязычный) |  |  | Установочное положение  
205 |  P_ARTICLE_INSTALLATION_LENGTH | Текст (значение с единицей измерения) | Длина | мм | Длина установки  
206 |  P_ARTICLE_FITTING_LENGTH_OF_THE_PROTECTION_TUBE | Текст (значение с единицей измерения) | Длина | мм | Длина установки: Защитная труба  
207 |  P_ARTICLE_INSTALLATION_DEPTH | Double |  |  | Глубина установки  
208 |  P_ARTICLE_UNIQUEID | Текст |  |  | Уникальный идентификатор изделия  
209 |  P_ARTICLE_CPMS_GUID | Текст |  |  | Уникальный внешний идентификатор изделия  
210 |  P_ARTICLE_INPUT_VOLUME_FLOW | Текст (значение с единицей измерения) | Объемный поток | m³/h | Входящий объемный поток  
211 |  P_ARTICLE_UNIT | Текст (многоязычный) |  |  | Единица измерения  
212 |  P_ARTICLE_PURCHASEPRICE_1 | Double |  |  | Закупочная цена/единица цены Валюта 1  
213 |  P_ARTICLE_PURCHASEPRICE_2 | Double |  |  | Закупочная цена/единица цены Валюта 2  
214 |  P_ARTICLE_PACKAGINGPRICE_1 | Double |  |  | Закупочная цена/упаковка Валюта 1  
215 |  P_ARTICLE_PACKAGINGPRICE_2 | Double |  |  | Закупочная цена/упаковка Валюта 2  
216 |  P_ARTICLE_TYPE_OF_USE | Текст (многоязычный) |  |  | Тип применения  
217 |  P_ARTICLE_RANGE_OF_APPLICATION | Текст (многоязычный) |  |  | Область применения  
218 |  P_ARTICLE_APPLICATION_AREA_OF_THE_CABLE | Текст (многоязычный) |  |  | Область применения: Кабель  
219 |  P_ARTICLE_POSSIBLE_APPLICATIONS | Текст (многоязычный) |  |  | Возможности использования  
220 |  P_ARTICLE_LOCATION | Текст (многоязычный) |  |  | Место использования  
221 |  P_ARTICLE_DUTY_CYCLE | Текст (значение с единицей измерения) | Время | s | Длительность включения  
222 |  P_ARTICLE_INRUSH_CURRENT | Текст (значение с единицей измерения) | Сила электрического тока | A | Ток включения  
223 |  P_ARTICLE_INRUSH_CURRENT_MAX | Текст (значение с единицей измерения) | Сила электрического тока | A | Ток включения, макс.  
224 |  P_ARTICLE_INRUSH_CURRENT_MIN | Текст (значение с единицей измерения) | Сила электрического тока | A | Ток включения, мин.  
225 |  P_ARTICLE_ELECTRICAL_INTERFACE | Текст (многоязычный) |  |  | Электрический интерфейс  
226 |  P_ARTICLE_ELECTRONIC_CONTROL_AVAILABLE | Текст (многоязычный) |  |  | Доступно электронное управление  
227 |  P_ARTICLE_RECOMMENDED_DIAMETER_OF_THE_CABLE | Текст (значение с единицей измерения) | Площадь | мм² | Рекомендованный диаметр кабеля  
228 |  P_ARTICLE_ULTIMATE_PRESSURE_MAX | Текст (значение с единицей измерения) | Давление | бар | Предельное давление, макс.  
229 |  P_ARTICLE_ULTIMATE_PRESSURE_MIN | Текст (значение с единицей измерения) | Давление | бар | Предельное давление, мин.  
230 |  P_ARTICLE_ULTIMATE_PRESSURE_SET | Текст (значение с единицей измерения) | Давление | бар | Предельное давление, заданное  
231 |  P_ARTICLE_ENERGY_EFFICIENCY_CLASS | Текст (многоязычный) |  |  | Класс энергоэффективности  
232 |  P_ARTICLE_ENERGY_EFFICIENCY_CLASS_MOTOR | Текст (многоязычный) |  |  | Класс энергоэффективности (двигатель)  
233 |  P_ARTICLE_ENERGY_EFFICIENCY_CLASS_CN | Текст (многоязычный) |  |  | Класс энергоэффективности CN  
234 |  P_ARTICLE_ENERGY_EFFICIENCY_CLASS_US | Текст (многоязычный) |  |  | Класс энергоэффективности US  
235 |  P_ARTICLE_DISASSEMBLE_ADDONPARTS4 | Long |  |  | Учитывать дополнительные части (спецификация изделий / данные изготовления)  
236 |  P_ARTICLE_DISASSEMBLE_ADDONPARTS2 | Long |  |  | Учитывать дополнительные части (спецификация изделий)  
237 |  P_ARTICLE_DISASSEMBLE_ADDONPARTS3 | Long |  |  | Учитывать дополнительные части (групповая спецификация изделий / данные изготовления)  
238 |  P_ARTICLE_DISASSEMBLE_ADDONPARTS | Long |  |  | Учитывать дополнительные части (групповая спецификация изделий)  
239 |  P_ARTICLE_REPLACEMENT_PART_DESCRIPTION | Текст (многоязычный) |  |  | Изделие для замены: Описание  
240 |  P_ARTICLE_REPLACEMENT_PART_DATE | Целое число (время) |  |  | Изделие для замены: Дата  
241 |  P_ARTICLE_REPLACEMENT_PART_NUMBER | Текст |  |  | Изделие для замены: Номер  
242 |  P_ARTICLE_REPLACEMENT_FOR_PRODUCT | Текст (многоязычный) |  |  | Изделие для замены: Оригинальное изделие  
243 |  P_ARTICLE_SPARE | Текст |  |  | Запчасть  
244 |  P_PART_CREATE_USER | Текст |  |  | Автор  
245 |  P_PART_CREATE | Текст |  |  | Автор / дата создания  
246 |  P_PART_TERMINAL_CREATE | Текст |  |  | Автор / дата создания (схема соединений)  
247 |  P_PART_CONSTRUCTION_CREATE | Текст |  |  | Автор / дата создания (схема сверления)  
248 |  P_PART_ACCESSORYLIST_CREATE | Текст |  |  | Автор / дата создания (список принадлежностей)  
249 |  P_PART_ACCESSORYPLACEMENT_CREATE | Текст |  |  | Автор / дата создания (размещение принадлежностей)  
250 |  P_PART_CREATE_DATE_UTC | Целое число (время) |  |  | Дата создания (UTC)  
251 |  P_ARTICLE_EXTERNAL_PLACEMENT | Булево (истина/ложь) |  |  | Внешнее размещение  
252 |  P_ARTICLE_EXTERNAL_DOCUMENT_1 | Текст |  |  | Внешний документ 1  
253 |  P_ARTICLE_EXTERNAL_DOCUMENT_2 | Текст |  |  | Внешний документ 2  
254 |  P_ARTICLE_EXTERNAL_DOCUMENT_3 | Текст |  |  | Внешний документ 3  
255 |  P_ARTICLE_EXTERNAL_DOCUMENT_4 | Текст |  |  | Внешний документ 4  
256 |  P_ARTICLE_EXTERNAL_DOCUMENT_5 | Текст |  |  | Внешний документ 5  
257 |  P_ARTICLE_EXTERNAL_DOCUMENT_6 | Текст |  |  | Внешний документ 6  
258 |  P_ARTICLE_EXTERNAL_DOCUMENT_7 | Текст |  |  | Внешний документ 7  
259 |  P_ARTICLE_EXTERNAL_DOCUMENT_8 | Текст |  |  | Внешний документ 8  
260 |  P_ARTICLE_EXTERNAL_DOCUMENT_9 | Текст |  |  | Внешний документ 9  
261 |  P_ARTICLE_EXTERNAL_DOCUMENT_10 | Текст |  |  | Внешний документ 10  
262 |  P_ARTICLE_EXTERNAL_DOCUMENT_11 | Текст |  |  | Внешний документ 11  
263 |  P_ARTICLE_EXTERNAL_DOCUMENT_12 | Текст |  |  | Внешний документ 12  
264 |  P_ARTICLE_EXTERNAL_DOCUMENT_13 | Текст |  |  | Внешний документ 13  
265 |  P_ARTICLE_EXTERNAL_DOCUMENT_14 | Текст |  |  | Внешний документ 14  
266 |  P_ARTICLE_EXTERNAL_DOCUMENT_15 | Текст |  |  | Внешний документ 15  
267 |  P_ARTICLE_EXTERNAL_DOCUMENT_16 | Текст |  |  | Внешний документ 16  
268 |  P_ARTICLE_EXTERNAL_DOCUMENT_17 | Текст |  |  | Внешний документ 17  
269 |  P_ARTICLE_EXTERNAL_DOCUMENT_18 | Текст |  |  | Внешний документ 18  
270 |  P_ARTICLE_EXTERNAL_DOCUMENT_19 | Текст |  |  | Внешний документ 19  
271 |  P_ARTICLE_EXTERNAL_DOCUMENT_20 | Текст |  |  | Внешний документ 20  
272 |  P_ARTICLE_FAMILY | Текст |  |  | Группа  
273 |  P_ARTICLE_CAPACITY | Текст (значение с единицей измерения) | Объем | m³ | Вместимость  
274 |  P_PART_ADDRESS_FAX | Текст |  |  | Факс  
275 |  P_ARTICLE_REMOTE_CONTROL_FUNCTION | Текст (многоязычный) |  |  | Функция дистанционного управления  
276 |  P_ARTICLE_FILTER_FINENESS | Текст (значение с единицей измерения) | Длина | мкм | Тонкость фильтрации  
277 |  P_ARTICLE_FLAME_RESISTANCE_ACCORDING_TO_STANDARD | Текст (многоязычный) |  |  | Огнестойкость (в соответствии со стандартом)  
278 |  P_ARTICLE_FREE_DATA_DESCRIPTION_#index | Текст (многоязычный) |  |  | Произвольные свойства: Отображаемое имя  
279 |  P_ARTICLE_FREE_DATA_UNIT_#index | Текст |  |  | Произвольн. свойства: Единица измерения  
280 |  P_ARTICLE_FREE_DATA_VALUE_#index | Текст (многоязычный) |  |  | Произв. свойство: Значение  
281 |  P_ARTICLE_FREQUENCY | Текст (значение с единицей измерения) | Частота | Гц | Частота  
282 |  P_ARTICLE_INPUT_VOLTAGE_FREQUENCY | Текст (значение с единицей измерения) | Частота | Гц | Частота (входное напряжение)  
283 |  P_ARTICLE_FREQUENCY_SIGNAL_PROCESSING | Текст (значение с единицей измерения) | Частота | Гц | Частота (обработка сигнала)  
284 |  P_ARTICLE_FREQUENCY_SIGNAL_PROCESSING_SET | Текст (значение с единицей измерения) | Частота | Гц | Частота (обработка сигнала), устанавливается  
285 |  P_ARTICLE_FREQUENCY_RANGE | Текст (значение с единицей измерения) | Частота | Гц | Диапазон частот  
286 |  P_ARTICLE_FREQUENCY_RANGE_MAX | Текст (значение с единицей измерения) | Частота | Гц | Диапазон частот, макс.  
287 |  P_ARTICLE_FREQUENCY_RANGE_MIN | Текст (значение с единицей измерения) | Частота | Гц | Диапазон частот, мин.  
288 |  P_ARTICLE_FUNKTION_IN_RUHESTELLUNG | Текст (многоязычный) |  |  | Функция в нейтральном положении  
289 |  P_ARTICLE_FUNCTIONGROUP | Текст |  |  | Группа функций  
290 |  P_ARTICLE_PUMPING_CAPACITY | Текст (значение с единицей измерения) | Объемный поток | m³/h | Пропускная способность  
291 |  P_ARTICLE_PUMPING_CAPACITY_OF_THE_OPERATING_LIQUID | Текст (значение с единицей измерения) | Объемный поток | m³/h | Пропускная способность рабочей жидкости  
292 |  P_ARTICLE_PUMPING_VOLUME | Текст (значение с единицей измерения) | Объемный поток | m³/h | Переносимый объем  
293 |  P_ARTICLE_FILLING_LEVEL | Текст (значение с единицей измерения) | Объем | m³ | Степень заполнения  
294 |  P_ARTICLE_FILLING_VOLUME | Текст (значение с единицей измерения) | Объем | m³ | Объем заполнения  
295 |  P_ARTICLE_BLOWER_PRESENT | Булево (истина/ложь) |  |  | Нагнетатель в наличии  
296 |  P_ARTICLE_FAN_AIR_FLOW | Текст (значение с единицей измерения) | Объемный поток | m³/h | Воздушный поток нагнетателя  
297 |  P_ARTICLE_SUITABLE_AS_MONITOR | Текст (многоязычный) |  |  | Подходит для реле  
298 |  P_ARTICLE_SUITABLE_FOR_KNX | Текст (многоязычный) |  |  | Пригоден для KNX  
299 |  P_ARTICLE_SUITABLE_FOR_CABLE_DIAMETERS | Текст (многоязычный) |  |  | Подходит для диаметра кабеля  
300 |  P_ARTICLE_SUITABLE_FOR_PCF_HCS_FIBRE_230_uM | Текст (значение с единицей измерения) | Длина | мкм | Подходит для волокна PCF / HCS 230 мкм  
301 |  P_ARTICLE_SUITABLE_FOR_PROTECTION_CLASS_IP | Long |  |  | Подходит для степени защиты (IP)  
302 |  P_ARTICLE_UNIT_CLASS | Текст (многоязычный) |  |  | Класс устройства  
303 |  P_ARTICLE_TOTAL_PRESSURE_DIFFERENCE_MAX | Текст (значение с единицей измерения) | Давление | бар | Полная разница давлений, макс.  
304 |  P_ARTICLE_TOTAL_PRESSURE_DIFFERENCE_MIN | Текст (значение с единицей измерения) | Давление | бар | Полная разница давлений, мин.  
305 |  P_ARTICLE_WEIGHT_TOTAL | Текст (значение с единицей измерения) | Масса | кг | Общий вес (изделие)  
306 |  P_ARTICLE_TOTAL_COOLING_CAPACITY_AT_35_35_C | Текст (значение с единицей измерения) | Мощность | Вт | Общая холодопроизводительность (при 35/35 °C)  
307 |  P_ARTICLE_TOTAL_VOLUME_FLOW | Текст (значение с единицей измерения) | Объемный поток | m³/h | Общий объемный поток  
308 |  P_ARTICLE_CRAFT_ELECTRICAL | Булево (истина/ложь) |  |  | Раздел 'Электротехника'  
309 |  P_ARTICLE_CRAFT_FLUID_UNDEFINED | Булево (истина/ложь) |  |  | Раздел 'Fluid (не определен)'  
310 |  P_ARTICLE_CRAFT_FLUID | Булево (истина/ложь) |  |  | Раздел 'Fluid-Техника'  
311 |  P_ARTICLE_CRAFT_GASTECHNOLOGY | Булево (истина/ложь) |  |  | Раздел 'Газовая техника'  
312 |  P_ARTICLE_CRAFT_HYDRAULICS | Булево (истина/ложь) |  |  | Раздел 'Гидравлика'  
313 |  P_ARTICLE_CRAFT_COOLINGLUBRICANT | Булево (истина/ложь) |  |  | Раздел 'Смазочно-охлаждающая жидкость'  
314 |  P_ARTICLE_CRAFT_COOLING | Булево (истина/ложь) |  |  | Раздел 'Охлаждение'  
315 |  P_ARTICLE_CRAFT_MECHANICS | Булево (истина/ложь) |  |  | Раздел 'Механика'  
316 |  P_ARTICLE_CRAFT_PNEUMATICS | Булево (истина/ложь) |  |  | Раздел 'Пневматика'  
317 |  P_ARTICLE_CRAFT_LUBRICATION | Булево (истина/ложь) |  |  | Раздел 'Смазка'  
318 |  P_ARTICLE_CRAFT_PROCESS | Булево (истина/ложь) |  |  | Раздел 'Технология производственных процессов'  
319 |  P_ARTICLE_WEIGHT | Double |  |  | Вес  
320 |  P_ARTICLE_WEIGHT_ITEM | Текст (значение с единицей измерения) | Масса | кг | Вес (изделие)  
321 |  P_ARTICLE_WEIGHT_OF_THE_INDIVIDUAL_ARTICLE_PACKAGING | Текст (значение с единицей измерения) | Масса | кг | Вес (упаковка отдельного изделия)  
322 |  P_ARTICLE_WEIGHT_OF_THE_PACKAGING | Текст (значение с единицей измерения) | Масса | кг | Вес (упаковка)  
323 |  P_ARTICLE_WEIGHT_KG_1000_M | Текст (значение с единицей измерения) | Масса | кг | Вес (в кг/1000 м)  
324 |  P_ARTICLE_THREAD_SIZE_METRIC | Текст (значение с единицей измерения) | Длина | мм | Размер резьбы (метрический)  
325 |  P_ARTICLE_THREAD_SIZE | Текст (значение с единицей измерения) | Длина | мм | Размер резьбы  
326 |  P_ARTICLE_THREAD_SIZE_FITTING | Текст (значение с единицей измерения) | Длина | мм | Размер резьбы (арматура)  
327 |  P_ARTICLE_MACRO | Текст |  |  | Графический макрос  
328 | P_ARTICLE_GROUPNUMBER | Текст |  |  | Номер группы  
329 |  P_ARTICLE_MANUFACTURER | Текст |  |  | Производитель  
330 |  P_ARTICLE_HYDRAULIC_POWER | Текст (значение с единицей измерения) | Мощность | kW | Гидравлическая мощность  
331 |  P_ARTICLE_HYDRAULIC_EFFICIENCY | Текст (значение с единицей измерения) | Процент | % | Гидравлический КПД  
332 |  P_ARTICLE_HEIGHT | Double |  |  | Высота  
333 |  P_ARTICLE_PROFILEHEIGHT | Double |  |  | Высота профиля, поперек  
334 |  P_ARTICLE_DISASSEMBLE2_MODE | Long |  |  | Разбить в спецификации изделий  
335 |  P_ARTICLE_DISASSEMBLE4_MODE | Long |  |  | Разбить в спецификации изделий (данные изготовления)  
336 |  P_ARTICLE_DISASSEMBLE_MODE | Long |  |  | Разбить на групповую спецификацию изделий  
337 |  P_ARTICLE_DISASSEMBLE3_MODE | Long |  |  | Разбить на групповую спецификацию изделий (данные изготовления)  
338 |  P_ARTICLE_SUPPRESSINPARTSLIST | Булево (истина/ложь) |  |  | Подавлять в спецификации  
339 |  P_ARTICLE_ACTUAL_TOTAL_VOLUME_FLOW | Текст (значение с единицей измерения) | Объемный поток | m³/h | Фактический общий объемный поток  
340 |  P_ARTICLE_ACTUAL_TOTAL_VOLUME_FLOW_MAX | Текст (значение с единицей измерения) | Объемный поток | m³/h | Фактический общий объемный поток, макс.  
341 |  P_ARTICLE_ACTUAL_TOTAL_VOLUME_FLOW_MIN | Текст (значение с единицей измерения) | Объемный поток | m³/h | Фактический общий объемный поток, мин.  
342 |  P_ARTICLE_ACTUAL_OUTPUT_HYDRAULIC | Текст (значение с единицей измерения) | Мощность | kW | Фактическая мощность (гидравлическая)  
343 |  P_ARTICLE_ACTUAL_OUTPUT_HYDRAULIC_MAX | Текст (значение с единицей измерения) | Мощность | kW | Фактическая мощность (гидравлическая), макс.  
344 |  P_ARTICLE_ACTUAL_OUTPUT_HYDRAULIC_MIN | Текст (значение с единицей измерения) | Мощность | kW | Фактическая мощность (гидравлическая), мин.  
345 |  P_ARTICLE_ACTUAL_OUTPUT_PNEUMATIC | Текст (значение с единицей измерения) | Мощность | kW | Фактическая мощность (пневматическая)  
346 |  P_ARTICLE_ACTUAL_OUTPUT_PNEUMATIC_MAX | Текст (значение с единицей измерения) | Мощность | kW | Фактическая мощность (пневматическая), макс.  
347 |  P_ARTICLE_ACTUAL_POWER_PNEUMATIC_MIN | Текст (значение с единицей измерения) | Мощность | kW | Фактическая мощность (пневматическая), мин.  
348 |  P_ARTICLE_BUS_SYSTEM_KNX_RADIO_COMPATIBLE | Текст (многоязычный) |  |  | KNX: Совместимый с радио KNX  
349 |  P_ARTICLE_BUS_SYSTEM_KNX_COMPATIBLE | Текст (многоязычный) |  |  | KNX: Совместимый  
350 |  P_ARTICLE_SUPPORTS_PROTOCOL_EIB_KNX | Текст (многоязычный) |  |  | KNX: Поддержка протокола EIB  
351 |  P_ARTICLE_SUPPORTS_PROTOCOL_OUTGOING_EIB_KNX | Текст (многоязычный) |  |  | KNX: Поддержка исходящего протокола EIB  
352 |  P_ARTICLE_SUPPORTS_PROTOCOL_INCOMING_EIB_KNX | Текст (многоязычный) |  |  | KNX: Поддержка входящего протокола EIB  
353 |  P_ARTICLE_CABLE_INCLUDED | Текст (многоязычный) |  |  | Кабель в комплекте  
354 |  P_ARTICLE_CROSS_SECTION_OF_THE_CABLE | Текст (значение с единицей измерения) | Площадь | мм² | Кабель: Поперечное сечение  
355 |  P_ARTICLE_CABLE_LEVEL | Текст (многоязычный) |  |  | Кабель: Уровень напряжения  
356 |  P_ARTICLE_CABLE_WINDER | Текст (многоязычный) |  |  | Намотка кабеля  
357 |  P_ARTICLE_CABLE_WINDER_AVAILABLE | Текст (многоязычный) |  |  | Намотка кабеля в наличии  
358 |  P_ARTICLE_OUTER_DIAMETER_OF_THE_CABLE | Текст (значение с единицей измерения) | Площадь | мм² | Внешний диаметр кабеля  
359 |  P_ARTICLE_OUTER_CABLE_DIAMETER_MAX | Текст (значение с единицей измерения) | Площадь | мм² | Внешний диаметр кабеля, макс.  
360 |  P_ARTICLE_CABLE_OUTER_DIAMETER_MIN | Текст (значение с единицей измерения) | Площадь | мм² | Внешний диаметр кабеля, мин.  
361 |  P_ARTICLE_CABLE_DATA | Текст (многоязычный) |  |  | Данные кабелей  
362 |  P_ARTICLE_CABLE_ENTRY_AVAILABLE | Текст (многоязычный) |  |  | Кабельный ввод в наличии  
363 |  P_ARTICLE_CABLE_DIAMETER | Текст (значение с единицей измерения) | Площадь | мм² | Диаметр кабеля  
364 |  P_ARTICLE_CABLE_ENTRY_INTO_THE_DEVICE | Текст (многоязычный) |  |  | Кабельный ввод в устройство  
365 |  P_ARTICLE_CABLE_LENGTH_MAX | Текст (значение с единицей измерения) | Длина | м | Длина кабеля, макс.  
366 |  P_ARTICLE_CABLE_LENGTH_LAID | Текст (значение с единицей измерения) | Длина | м | Длина кабеля, проложенного  
367 |  P_ARTICLE_COLOUR_OF_THE_CABLE_SHEATH | Текст (многоязычный) |  |  | Оболочка кабеля: Цвет  
368 |  P_ARTICLE_CAPACITIVE_LOAD | Текст (значение с единицей измерения) | Электрическая емкость | µF | Емкостная нагрузка  
369 |  P_ARTICLE_CHARACTERISTIC | Текст (многоязычный) |  |  | Графическая характеристика  
370 |  P_ARTICLE_REPORT_IDENTIFIER | Текст |  |  | Идентификатор отчетов  
371 |  P_ARTICLE_LABELLING | Текст (многоязычный) |  |  | Идентификатор  
372 |  P_ARTICLE_CLAMP_COLOUR | Текст (многоязычный) |  |  | Клемма: Цвет  
373 |  P_ARTICLE_TERMINAL_POTENTIAL | Текст (значение с единицей измерения) | Электрическое напряжение | V | Клеммный потенциал  
374 |  P_ARTICLE_CLIMATE_CLASS | Текст (многоязычный) |  |  | Климатический класс  
375 |  P_ARTICLE_CONTACT_POTENTIAL | Текст (значение с единицей измерения) | Электрическое напряжение | V | Контактный потенциал  
376 |  P_PART_ADDRESS_NUMBER | Текст |  |  | Номер клиента  
377 |  P_PART_ADDRESS_SHORTNAME | Текст |  |  | Краткое имя  
378 |  P_ARTICLE_STORAGE_TRANSPORT_AND_PACKAGING_REQUIREMENT | Текст (многоязычный) |  |  | Хранение, транспортировка и упаковка (требование)  
379 |  P_PART_ADDRESS_STATE | Текст |  |  | Страна  
380 |  P_PART_ADDRESS_LONGNAME | Текст |  |  | Полное имя  
381 |  P_ARTICLE_LIFETIME | Текст |  |  | Срок службы  
382 |  P_ARTICLE_POWER_CONSUMPTION | Текст (значение с единицей измерения) | Мощность | Вт | Потребление мощности  
383 |  P_ARTICLE_MAX_POWER_CONSUMPTION | Текст (значение с единицей измерения) | Мощность | Вт | Потребление мощности, макс.  
384 |  P_ARTICLE_POWER_REQUIREMENT_MAX | Текст (значение с единицей измерения) | Мощность | Вт | Потребность в мощности, макс.  
385 |  P_ARTICLE_POWER_REQUIREMENT_MIN | Текст (значение с единицей измерения) | Мощность | Вт | Потребность в мощности, мин.  
386 |  P_ARTICLE_POWER_DESCRIPTION | Текст (многоязычный) |  |  | Описание возможностей (функциональный элемент, устройство)  
387 |  P_ARTICLE_PERFORMANCE_DESCRIPTION | Текст (многоязычный) |  |  | Описание возможностей, стандартизированное: Описание (устройство, услуга, сервис)  
388 |  P_ARTICLE_POWER_GROUP_ITEM_NUMBER_LGPOSNR | Текст (многоязычный) |  |  | Описание возможностей, стандартизированное: Номер позиции группы услуг  
389 |  P_ARTICLE_POSITION_NUMBER_STLB | Текст (многоязычный) |  |  | Описание возможностей, стандартизированное: Номер позиции (устройство, услуга, сервис)  
390 |  P_ARTICLE_POSITION_KEYWORD | Текст (многоязычный) |  |  | Описание возможностей, стандартизированное: Ключевое слово позиции (устройство, услуга, сервис)  
391 |  P_ARTICLE_SERVICE_UNIT | Текст (многоязычный) |  |  | Единица услуги (перечень работ и услуг, подлежащих выполнению)  
392 |  P_ARTICLE_POWER_FACTOR | Double |  |  | Коэффициент мощности (cos phi)  
393 |  P_ARTICLE_CIRCUIT_BREAKER_TEST_AVAILABLE | Текст (многоязычный) |  |  | Проверка силового выключателя доступна  
394 |  P_ARTICLE_POWER_CONTROL | Текст (многоязычный) |  |  | Регулирование мощности  
395 |  P_ARTICLE_LV_IDENTIFIER | Long |  |  | Идентификатор перечня работ и услуг, подлежащих выполнению  
396 |  P_ARTICLE_CONDUCTOR_STRUCTURE_CABLE | Текст (многоязычный) |  |  | Конструкция провода (кабель)  
397 |  P_ARTICLE_CONDUCTOR_CROSS_SECTION | Текст (значение с единицей измерения) | Площадь | мм² | Поперечное сечение проводника  
398 |  P_ARTICLE_CONDUCTIVITY | Текст |  |  | Проводимость (при +20 °C)  
399 |  P_PART_LASTCHANGE_USER | Текст |  |  | Последний обработчик  
400 |  P_PART_LASTCHANGE | Текст |  |  | Последний обработчик / дата изменения  
401 |  P_PART_ADDRESS_LASTCHANGE | Текст |  |  | Последний обработчик / дата изменения (адрес)  
402 |  P_PART_TERMINAL_LASTCHANGE | Текст |  |  | Последний обработчик / дата изменения (схема соединений)  
403 |  P_PART_CONSTRUCTION_LASTCHANGE | Текст |  |  | Последний обработчик / дата изменения (схема сверления)  
404 |  P_PART_ACCESSORYLIST_LASTCHANGE | Текст |  |  | Последний обработчик / дата изменения (список принадлежностей)  
405 |  P_PART_ACCESSORYPLACEMENT_LASTCHANGE | Текст |  |  | Последний обработчик / дата изменения (размещение принадлежностей)  
406 |  P_ARTICLE_SUPPLIER | Текст |  |  | Поставщик  
407 |  P_ARTICLE_SUPPLIER_BATCH_NUMBER | Текст (многоязычный) |  |  | Номер партии поставщика  
408 |  P_ARTICLE_DELIVERYLENGTH | Double |  |  | Поставляемая длина  
409 |  P_ARTICLE_HOLE_PATTERN | Текст (многоязычный) |  |  | Схема расположения отверстий  
410 |  P_ARTICLE_LENGTH_MAX | Текст (значение с единицей измерения) | Длина | м | Длина, макс.  
411 |  P_ARTICLE_LENGTH_MIN | Текст (значение с единицей измерения) | Длина | м | Длина, мин.  
412 |  P_ARTICLE_MANUAL_CONTROLS | Текст (многоязычный) |  |  | Ручные элементы управления  
413 |  P_ARTICLE_MASS | Текст (значение с единицей измерения) | Масса | кг | Масса  
414 |  P_ARTICLE_MASS_FLOW | Текст (значение с единицей измерения) | Массовый поток | g/min | Массовый поток  
415 |  P_ARTICLE_MASS_MOMENT_OF_INERTIA_OF_THE_LOAD | Текст (значение с единицей измерения) | Момент инерции | kg*m² | Момент инерции массы груза  
416 |  P_ARTICLE_PACKAGINGQUANTITY | Double |  |  | Количество/упаковка  
417 |  P_ARTICLE_QUANTITYUNIT | Текст (многоязычный) |  |  | Един. измерения  
418 |  P_ARTICLE_MEASURING_RANGE | Текст (значение с единицей измерения) |  |  | Область измерений  
419 |  P_ARTICLE_MEASURING_RANGE_SCALE_LENGTH | Текст (значение с единицей измерения) |  |  | Область измерения / Длина шкалы  
420 |  P_ARTICLE_MEASURING_RANGE_MAX_ | Текст (значение с единицей измерения) | Процент | % | Область измерения: Макс.  
421 |  P_ARTICLE_MEASURING_RANGE_MIN | Текст (значение с единицей измерения) | Процент | % | Область измерения: Мин.  
422 |  P_ARTICLE_MEASURING_RANGE_OF_THE_OPERATING_VOLUME_FLOW_RATE | Текст (значение с единицей измерения) | Объемный поток | m³/s | Область измерения: Рабочий объемный расход  
423 |  P_ARTICLE_MEASURING_RANGE_OF_DENSITY | Текст (значение с единицей измерения) | Масса на объем | kg/m³ | Область измерения: Плотность  
424 |  P_ARTICLE_MEASURING_RANGE_OF_PRESSURE | Текст (значение с единицей измерения) | Давление | бар | Область измерения: Давление  
425 |  P_ARTICLE_MEASURING_RANGE_OF_DYNAMIC_VISCOSITY | Текст (значение с единицей измерения) | Динамическая вязкость | Pa*s | Область измерения: Динамическая вязкость  
426 |  P_ARTICLE_MEASURING_RANGE_OF_HUMIDITY_PERCENTRH | Текст (значение с единицей измерения) | Относительная влажность воздуха | %RH | Область измерения: Влажность (в % относительной влажности)  
427 |  P_ARTICLE_MEASURING_RANGE_OF_THE_WEIGHT | Текст (значение с единицей измерения) | Масса | г | Область измерения: Вес  
428 |  P_ARTICLE_MEASURING_RANGE_OF_THE_CONCENTRATION_MEASUREMENT | Текст (значение с единицей измерения) | Процент | % | Область измерения: Измерение концентрации  
429 |  P_ARTICLE_MEASURING_RANGE_OF_THE_MASS_FLOW_RATE | Текст (значение с единицей измерения) | Стандартный объемный расход | ln/min | Область измерения: Массовый расход  
430 |  P_ARTICLE_MEASURING_RANGE_OF_THE_QUANTITY | Текст (значение с единицей измерения) |  |  | Область измерения: Количество  
431 |  P_ARTICLE_LEVEL_MEASURING_RANGE | Текст (значение с единицей измерения) |  |  | Область измерения: Уровень  
432 |  P_ARTICLE_MEASURING_RANGE_OF_STANDARD_VOLUME_FLOW | Текст (значение с единицей измерения) | Объемный поток | m³/s | Область измерения: Измерение стандартного объемного расхода  
433 |  P_ARTICLE_MEASURING_RANGE_UPPER_LIMIT_VALUE | Текст (значение с единицей измерения) | Процент | % | Область измерения: Верхн. пред. значение  
434 |  P_ARTICLE_MEASURING_RANGE_OF_THE_SWITCHING_DISTANCE | Текст (значение с единицей измерения) | Длина | мм | Область измерения: Интервал включения  
435 |  P_ARTICLE_MEASURING_RANGE_OF_TEMPERATURE | Текст (значение с единицей измерения) | Температура | °C | Область измерения: Температура  
436 |  P_ARTICLE_MEASURING_RANGE_LOWER_LIMIT_VALUE | Текст (значение с единицей измерения) | Процент | % | Область измерения: Нижн. пред. значение  
437 |  P_ARTICLE_MEASURING_RANGE_OF_RATIO_MEASUREMENT | Текст (значение с единицей измерения) | Процент | % | Область измерения: Измерение соотношения  
438 |  P_ARTICLE_MEASURING_RANGE_OF_THE_VOLUME_MEASUREMENT | Текст (значение с единицей измерения) | Объемный поток | m³/s | Область измерения: Измерение объема  
439 |  P_ARTICLE_MEASURING_ACCURACY | Текст (многоязычный) |  |  | Точность измерения  
440 |  P_ARTICLE_MEASURED_VARIABLE | Текст (многоязычный) |  |  | Измеряемая величина  
441 |  P_ARTICLE_CABLE_PIPE_TRANSMITTER_CONNECTION | Текст (многоязычный) |  |  | Измерительный преобразователь: Присоединение к линии (кабель / труба)  
442 |  P_ARTICLE_METHOD | Текст (многоязычный) |  |  | Метод  
443 |  P_ARTICLE_METHOD_NAME | Текст (многоязычный) |  |  | Название метода  
444 |  P_ARTICLE_MIDDLEOFFSET | Double |  |  | Несовпадение центров  
445 |  P_ARTICLE_MOUNTINGSITE | Long (список выбора) |  |  | Монтажная поверхность  
446 |  P_ARTICLE_NOMINAL_MOTOR_POWER | Текст (значение с единицей измерения) | Мощность | kW | Номинальная мощность двигателя  
447 |  P_PART_CONSTRUCTION_NAME | Текст |  |  | Имя  
448 |  P_PART_ADDRESS_NAME1 | Текст |  |  | Имя 1  
449 |  P_PART_ADDRESS_NAME2 | Текст |  |  | Имя 2  
450 |  P_PART_ADDRESS_NAME3 | Текст |  |  | Имя 3  
451 |  P_PART_TERMINAL_NAME | Текст |  |  | Имя (схема соединений)  
452 |  P_PART_ACCESSORYLIST_NAME | Текст |  |  | Имя (список принадлежностей)  
453 |  P_PART_ACCESSORYPLACEMENT_NAME | Текст |  |  | Имя (размещение принадлежностей)  
454 |  P_ARTICLE_RATED_OUTPUT_TORQUE | Текст (значение с единицей измерения) | Работа | Н∙м | Номинальный вращающий момент на выходном валу  
455 |  P_ARTICLE_RATED_DRIVING_TORQUE | Текст (значение с единицей измерения) | Работа | Н∙м | Номинальный вращающий момент привода  
456 |  P_ARTICLE_NOMINAL_TOTAL_VOLUME_FLOW | Текст (значение с единицей измерения) | Объемный поток | m³/h | Номинальный общий объемный поток  
457 |  P_ARTICLE_NOMINAL_SUCTION_PRESSURE | Текст (значение с единицей измерения) | Давление | бар | Номинальное давление всасывания  
458 |  P_ARTICLE_RATED_SPEED | Текст (значение с единицей измерения) | Частота вращения | U/min | Номинальная частота вращения  
459 |  P_ARTICLE_NOMINAL_PRESSURE | Текст (значение с единицей измерения) | Давление | бар | Номинальное давление  
460 |  P_ARTICLE_NOMINAL_PRESSURE_SERIES | Текст (значение с единицей измерения) |  |  | Ряд номинального давления  
461 |  P_ARTICLE_RATED_POWER_KW | Текст (значение с единицей измерения) | Мощность | kW | Номинальная мощность  
462 |  P_ARTICLE_NOMINAL_POWER_HYDRAULIC | Текст (значение с единицей измерения) | Мощность | kW | Номинальная мощность (гидравлическая)  
463 |  P_ARTICLE_MAX_RATED_POWER | Текст (значение с единицей измерения) | Мощность | kW | Номинальная мощность (в кВт), макс.  
464 |  P_ARTICLE_RATED_POWER_MIN | Текст (значение с единицей измерения) | Мощность | kW | Номинальная мощность (в кВт), мин.  
465 |  P_ARTICLE_NOMINAL_CAPACITY_PNEUMATIC | Текст (значение с единицей измерения) | Мощность | kW | Номинальная мощность (пневматическая)  
466 |  P_ARTICLE_NOMINAL_POWER_CONSUMPTION | Текст (значение с единицей измерения) | Мощность | kW | Номинальное потребление мощности  
467 |  P_ARTICLE_NOMINAL_POWER_REQUIREMENT | Текст (значение с единицей измерения) | Мощность | Вт | Номинальная потребность в мощности  
468 |  P_ARTICLE_RATED_VOLTAGE | Текст (значение с единицей измерения) | Электрическое напряжение | V | Номинальное напряжение  
469 |  P_ARTICLE_RATED_VOLTAGE_OF_THE_LOAD_CIRCUIT | Текст (значение с единицей измерения) | Электрическое напряжение | V | Номинальное напряжение (цепь нагрузки)  
470 |  P_ARTICLE_RATED_VOLTAGE_OF_THE_CONTROL_CIRCUIT | Текст (значение с единицей измерения) | Электрическое напряжение | V | Номинальное напряжение (цепь управления)  
471 |  P_ARTICLE_RATED_VOLTAGE_FOR_AC_50_HZ | Текст (значение с единицей измерения) | Электрическое напряжение | V | Номинальное напряжение (при переменном токе 50 Гц)  
472 |  P_ARTICLE_RATED_VOLTAGE_FOR_AC | Текст (значение с единицей измерения) | Электрическое напряжение | V | Номинальное напряжение (при переменном токе)  
473 |  P_ARTICLE_RATED_VOLTAGE_FOR_DC | Текст (значение с единицей измерения) | Электрическое напряжение | V | Номинальное напряжение (при постоянном токе)  
474 |  P_ARTICLE_NOMINAL_CURRENT | Текст (значение с единицей измерения) | Сила электрического тока | A | Номинальный ток  
475 |  P_ARTICLE_MAX_RATED_CURRENT | Текст (значение с единицей измерения) | Сила электрического тока | A | Номинальный ток, макс.  
476 |  P_ARTICLE_RATED_CURRENT_MIN | Текст (значение с единицей измерения) | Сила электрического тока | A | Номинальный ток, мин.  
477 |  P_ARTICLE_RATED_CURRENT_CONSUMPTION | Текст (значение с единицей измерения) | Сила электрического тока | A | Номинальное потребление тока  
478 |  P_ARTICLE_NOMINAL_VOLUME_FLOW | Текст (значение с единицей измерения) | Объемный поток | m³/h | Номинальный объемный поток  
479 |  P_ARTICLE_NOMINAL_VOLUME_FLOW_OF_THE_SUCTION_SIDE | Текст (значение с единицей измерения) | Объемный поток | m³/h | Номинальный объемный поток (сторона всасывания)  
480 |  P_ARTICLE_NOMINAL_VOLUMETRIC_FLOW_OF_COMPRESSED_AIR | Текст (значение с единицей измерения) | Объемный поток | m³/h | Номинальный объемный поток (сжатый воздух)  
481 |  P_ARTICLE_NOMINAL_WIDTH_CONNECTION_SIZE | Текст (значение с единицей измерения) |  |  | Номинальная ширина / размер вывода устройства  
482 |  P_ARTICLE_NOMINAL_WIDTH | Текст (значение с единицей измерения) | Длина | мм | Номинальная ширина / диаметр  
483 |  P_ARTICLE_EMERGENCY_CONTROL_FUNCTION | Текст (многоязычный) |  |  | Функция аварийного останова  
484 |  P_ARTICLE_EMERGENCY_CONTROL_FUNCTION_CLOSED | Текст (многоязычный) |  |  | Функция аварийного останова (закрыта)  
485 |  P_ARTICLE_EMERGENCY_CONTROL_FUNCTION_OPEN | Текст (многоязычный) |  |  | Функция аварийного останова (открыта)  
486 |  P_ARTICLE_NOMINAL_COOLING_PERFORMANCE_L35W10_200L_H | Текст (значение с единицей измерения) | Мощность | Вт | Полезная холодопроизводительность (L35W10 200 л/ч)  
487 |  P_ARTICLE_NOMINAL_COOLING_PERFORMANCE_L35W10_400L_H | Текст (значение с единицей измерения) | Мощность | Вт | Полезная холодопроизводительность (L35W10 400 л/ч)  
488 |  P_ARTICLE_SURFACE_COATING | Текст (многоязычный) |  |  | Покрытие поверхности  
489 |  P_ARTICLE_OHMIC_RESISTANCE | Текст (значение с единицей измерения) | Электрическое сопротивление | Ω | Омическое сопротивление  
490 |  P_ARTICLE_NUMBER_OF_PCF_METHODS | Текст (значение с единицей измерения) | Количество | Stück | PCF: Количество методов вычисления  
491 |  P_ARTICLE_PCF_PRODUCT_CARBON_FOOTPRINT_CALCULATION | Текст (значение с единицей измерения) |  |  | PCF: Вычисление  
492 |  P_ARTICLE_PCF_CALCULATION_METHOD | Текст (значение с единицей измерения) |  |  | PCF: Метод вычисления  
493 |  P_ARTICLE_PCF_REFERENCE_VALUE_FOR_THE_CALCULATION | Текст (значение с единицей измерения) |  |  | PCF: Базовый параметр для вычисления  
494 |  P_ARTICLE_PCF_CO2EQ | Текст (значение с единицей измерения) |  |  | PCF: Эквивалент CO2  
495 |  P_ARTICLE_PCF_LIFE_CYCLE_PHASE | Текст (значение с единицей измерения) |  |  | PCF: Фаза жизненного цикла  
496 |  P_ARTICLE_PCF_QUANTITY_FOR_CALCULATION | Текст (значение с единицей измерения) |  |  | PCF: Указание количества для вычисления  
497 |  P_ARTICLE_PCF_GOODS_TRANSFER_ADDRESS | Текст (значение с единицей измерения) |  |  | PCF: Адрес передачи товара  
498 |  P_PART_ADDRESS_ZIPPOBOX | Текст |  |  | Почт. индекс (почт. ящик)  
499 |  P_PART_ADDRESS_ZIPTOWN | Текст |  |  | Почтовый индекс (место жительства)  
500 |  P_ARTICLE_MOUNTINGSPACE | Double |  |  | Занимаемая площадь  
501 |  P_ARTICLE_PNEUMATICALLY_OPERATED | Текст (многоязычный) |  |  | Эксплуатировать пневматически  
502 |  P_ARTICLE_POLE_NUMBER | Long |  |  | Количество полюсов  
503 |  P_ARTICLE_POSITION_NUMBER_MANUFACTURER | Текст (многоязычный) |  |  | Номер позиции (производитель)  
504 |  P_PART_ADDRESS_POBOX | Текст |  |  | Почт. ящик  
505 |  P_ARTICLE_PRICEUNIT | Long |  |  | Цена единицы  
506 |  P_ARTICLE_PRODUCTGROUP | Long (список выбора) |  |  | [Группа продуктов](xmlexport_o_productgroups.md#P_ARTICLE_PRODUCTGROUP)  
507 |  P_ARTICLE_PRODUCTTOPGROUP | Long (список выбора) |  |  | [Главная группа продуктов](xmlexport_o_productgroups.md#P_ARTICLE_PRODUCTTOPGROUP)  
508 |  P_ARTICLE_PRODUCT_TYPE | Текст (многоязычный) |  |  | Тип продукта  
509 |  P_ARTICLE_PRODUCTSUBGROUP | Long (список выбора) |  |  | [Подгруппа продуктов](xmlexport_o_productgroups.md#P_ARTICLE_PRODUCTSUBGROUP)  
510 |  P_ARTICLE_UPPER_PROCESS_PRESSURE_LIMIT_ABSOLUTE_PRESSURE | Текст (значение с единицей измерения) | Давление | Па | Технологическое давление (абсолютное давление), макс.  
511 |  P_ARTICLE_UPPER_PROCESS_PRESSURE_LIMIT_GAUGE_PRESSURE | Текст (значение с единицей измерения) | Давление | Па | Технологическое давление (избыточное давление), макс.  
512 |  P_ARTICLE_TEST_VOLTAGE | Текст (значение с единицей измерения) | Электрическое напряжение | V | Испытательное напряжение  
513 |  P_ARTICLE_CROSS_SECTION | Текст (значение с единицей измерения) | Площадь | мм² | Поперечное сечение  
514 |  P_ARTICLE_CROSS_SECTION_MAX | Текст (значение с единицей измерения) | Площадь | мм² | Поперечное сечение, макс.  
515 |  P_ARTICLE_DISCOUNT | Double |  |  | Скидка  
516 |  P_ARTICLE_PURITY_CLASS_OF_THE_PRESSURISED_FLUID | Текст (многоязычный) |  |  | Класс чистоты жидкости под давлением  
517 |  P_ARTICLE_PURITY_CLASS_OF_THE_CONTROL_OIL | Текст (многоязычный) |  |  | Класс чистоты масла в линии управления  
518 |  P_ARTICLE_FEEDBACK_CONTACT_PRESENT | Текст (многоязычный) |  |  | Контакт ответа в наличии  
519 |  P_ARTICLE_POSITION_FEEDBACK_SIGNAL_ACTUATOR | Текст (многоязычный) |  |  | Ответ в наличии  
520 |  P_ARTICLE_PLCGROUP_DATALENGTH_OUTPUTS | Текст |  |  | Устройство ПЛК: Длина данных (выходы)  
521 |  P_ARTICLE_PLCGROUP_DATALENGTH_INPUTS | Текст |  |  | Устройство ПЛК: Длина данных (входы)  
522 |  P_ARTICLE_PLCDEVICENUMBER_1 | Текст |  |  | Подустройство ПЛК 1: На позиции / разъем  
523 |  P_ARTICLE_PLCGROUP_DATALENGTH_OUTPUTS_1 | Текст |  |  | Подустройство ПЛК 1: Длина данных (выходы)  
524 |  P_ARTICLE_PLCGROUP_DATALENGTH_INPUTS_1 | Текст |  |  | Подустройство ПЛК 1: Длина данных (входы)  
525 |  P_ARTICLE_PLCGROUP_INDEXINFILE_1 | Текст |  |  | Подустройство ПЛК 1: описание устройства: индекс в файле  
526 |  P_ARTICLE_PLCDEVICENAME_1 | Текст |  |  | Подустройство ПЛК 1: Имя  
527 |  P_ARTICLE_PLCGROUP_TYPIDENTIFIER_1 | Текст |  |  | Подустройство ПЛК 1: обозначение типа ПЛК  
528 |  P_ARTICLE_PLCDEVICENUMBER_2 | Текст |  |  | Подустройство ПЛК 2: На позиции / разъем  
529 |  P_ARTICLE_PLCGROUP_DATALENGTH_OUTPUTS_2 | Текст |  |  | Подустройство ПЛК 2: Длина данных (выходы)  
530 |  P_ARTICLE_PLCGROUP_DATALENGTH_INPUTS_2 | Текст |  |  | Подустройство ПЛК 2: Длина данных (входы)  
531 |  P_ARTICLE_PLCGROUP_INDEXINFILE_2 | Текст |  |  | Подустройство ПЛК 2: описание устройства: индекс в файле  
532 |  P_ARTICLE_PLCDEVICENAME_2 | Текст |  |  | Подустройство ПЛК 2: Имя  
533 |  P_ARTICLE_PLCGROUP_TYPIDENTIFIER_2 | Текст |  |  | Подустройство ПЛК 2: обозначение типа ПЛК  
534 |  P_ARTICLE_PLCDEVICENUMBER_3 | Текст |  |  | Подустройство ПЛК 3: На позиции / разъем  
535 |  P_ARTICLE_PLCGROUP_DATALENGTH_OUTPUTS_3 | Текст |  |  | Подустройство ПЛК 3: Длина данных (выходы)  
536 |  P_ARTICLE_PLCGROUP_DATALENGTH_INPUTS_3 | Текст |  |  | Подустройство ПЛК 3: Длина данных (входы)  
537 |  P_ARTICLE_PLCGROUP_INDEXINFILE_3 | Текст |  |  | Подустройство ПЛК 3: описание устройства: индекс в файле  
538 |  P_ARTICLE_PLCDEVICENAME_3 | Текст |  |  | Подустройство ПЛК 3: Имя  
539 |  P_ARTICLE_PLCGROUP_TYPIDENTIFIER_3 | Текст |  |  | Подустройство ПЛК 3: обозначение типа ПЛК  
540 |  P_ARTICLE_PLCDEVICENUMBER_4 | Текст |  |  | Подустройство ПЛК 4: На позиции / разъем  
541 |  P_ARTICLE_PLCGROUP_DATALENGTH_OUTPUTS_4 | Текст |  |  | Подустройство ПЛК 4: Длина данных (выходы)  
542 |  P_ARTICLE_PLCGROUP_DATALENGTH_INPUTS_4 | Текст |  |  | Подустройство ПЛК 4: Длина данных (входы)  
543 |  P_ARTICLE_PLCGROUP_INDEXINFILE_4 | Текст |  |  | Подустройство ПЛК 4: описание устройства: индекс в файле  
544 |  P_ARTICLE_PLCDEVICENAME_4 | Текст |  |  | Подустройство ПЛК 4: Имя  
545 |  P_ARTICLE_PLCGROUP_TYPIDENTIFIER_4 | Текст |  |  | Подустройство ПЛК 4: обозначение типа ПЛК  
546 |  P_ARTICLE_PLCDEVICENUMBER_5 | Текст |  |  | Подустройство ПЛК 5: На позиции / разъем  
547 |  P_ARTICLE_PLCGROUP_DATALENGTH_OUTPUTS_5 | Текст |  |  | Подустройство ПЛК 5: Длина данных (выходы)  
548 |  P_ARTICLE_PLCGROUP_DATALENGTH_INPUTS_5 | Текст |  |  | Подустройство ПЛК 5: Длина данных (входы)  
549 |  P_ARTICLE_PLCGROUP_INDEXINFILE_5 | Текст |  |  | Подустройство ПЛК 5: описание устройства: индекс в файле  
550 |  P_ARTICLE_PLCDEVICENAME_5 | Текст |  |  | Подустройство ПЛК 5: Имя  
551 |  P_ARTICLE_PLCGROUP_TYPIDENTIFIER_5 | Текст |  |  | Подустройство ПЛК 5: обозначение типа ПЛК  
552 |  P_ARTICLE_PLCDEVICENUMBER_6 | Текст |  |  | Подустройство ПЛК 6: На позиции / разъем  
553 |  P_ARTICLE_PLCGROUP_DATALENGTH_OUTPUTS_6 | Текст |  |  | Подустройство ПЛК 6: Длина данных (выходы)  
554 |  P_ARTICLE_PLCGROUP_DATALENGTH_INPUTS_6 | Текст |  |  | Подустройство ПЛК 6: Длина данных (входы)  
555 |  P_ARTICLE_PLCGROUP_INDEXINFILE_6 | Текст |  |  | Подустройство ПЛК 6: описание устройства: индекс в файле  
556 |  P_ARTICLE_PLCDEVICENAME_6 | Текст |  |  | Подустройство ПЛК 6: Имя  
557 |  P_ARTICLE_PLCGROUP_TYPIDENTIFIER_6 | Текст |  |  | Подустройство ПЛК 6: обозначение типа ПЛК  
558 |  P_ARTICLE_PLCDEVICENUMBER_7 | Текст |  |  | Подустройство ПЛК 7: На позиции / разъем  
559 |  P_ARTICLE_PLCGROUP_DATALENGTH_OUTPUTS_7 | Текст |  |  | Подустройство ПЛК 7: Длина данных (выходы)  
560 |  P_ARTICLE_PLCGROUP_DATALENGTH_INPUTS_7 | Текст |  |  | Подустройство ПЛК 7: Длина данных (входы)  
561 |  P_ARTICLE_PLCGROUP_INDEXINFILE_7 | Текст |  |  | Подустройство ПЛК 7: описание устройства: индекс в файле  
562 |  P_ARTICLE_PLCDEVICENAME_7 | Текст |  |  | Подустройство ПЛК 7: Имя  
563 |  P_ARTICLE_PLCGROUP_TYPIDENTIFIER_7 | Текст |  |  | Подустройство ПЛК 7: обозначение типа ПЛК  
564 |  P_ARTICLE_PLCDEVICENUMBER_8 | Текст |  |  | Подустройство ПЛК 8: На позиции / разъем  
565 |  P_ARTICLE_PLCGROUP_DATALENGTH_OUTPUTS_8 | Текст |  |  | Подустройство ПЛК 8: Длина данных (выходы)  
566 |  P_ARTICLE_PLCGROUP_DATALENGTH_INPUTS_8 | Текст |  |  | Подустройство ПЛК 8: Длина данных (входы)  
567 |  P_ARTICLE_PLCGROUP_INDEXINFILE_8 | Текст |  |  | Подустройство ПЛК 8: описание устройства: индекс в файле  
568 |  P_ARTICLE_PLCDEVICENAME_8 | Текст |  |  | Подустройство ПЛК 8: Имя  
569 |  P_ARTICLE_PLCGROUP_TYPIDENTIFIER_8 | Текст |  |  | Подустройство ПЛК 8: обозначение типа ПЛК  
570 |  P_ARTICLE_PLCDEVICENUMBER_9 | Текст |  |  | Подустройство ПЛК 9: На позиции / разъем  
571 |  P_ARTICLE_PLCGROUP_DATALENGTH_OUTPUTS_9 | Текст |  |  | Подустройство ПЛК 9: Длина данных (выходы)  
572 |  P_ARTICLE_PLCGROUP_DATALENGTH_INPUTS_9 | Текст |  |  | Подустройство ПЛК 9: Длина данных (входы)  
573 |  P_ARTICLE_PLCGROUP_INDEXINFILE_9 | Текст |  |  | Подустройство ПЛК 9: описание устройства: индекс в файле  
574 |  P_ARTICLE_PLCDEVICENAME_9 | Текст |  |  | Подустройство ПЛК 9: Имя  
575 |  P_ARTICLE_PLCGROUP_TYPIDENTIFIER_9 | Текст |  |  | Подустройство ПЛК 9: обозначение типа ПЛК  
576 |  P_ARTICLE_PLCDEVICENUMBER_10 | Текст |  |  | Подустройство ПЛК 10: На позиции / разъем  
577 |  P_ARTICLE_PLCGROUP_DATALENGTH_OUTPUTS_10 | Текст |  |  | Подустройство ПЛК 10: Длина данных (выходы)  
578 |  P_ARTICLE_PLCGROUP_DATALENGTH_INPUTS_10 | Текст |  |  | Подустройство ПЛК 10: Длина данных (входы)  
579 |  P_ARTICLE_PLCGROUP_INDEXINFILE_10 | Текст |  |  | Подустройство ПЛК 10: описание устройства: индекс в файле  
580 |  P_ARTICLE_PLCDEVICENAME_10 | Текст |  |  | Подустройство ПЛК 10: Имя  
581 |  P_ARTICLE_PLCGROUP_TYPIDENTIFIER_10 | Текст |  |  | Подустройство ПЛК 10: обозначение типа ПЛК  
582 |  P_ARTICLE_PLCDEVICENUMBER_11 | Текст |  |  | Подустройство ПЛК 11: На позиции / разъем  
583 |  P_ARTICLE_PLCGROUP_DATALENGTH_OUTPUTS_11 | Текст |  |  | Подустройство ПЛК 11: Длина данных (выходы)  
584 |  P_ARTICLE_PLCGROUP_DATALENGTH_INPUTS_11 | Текст |  |  | Подустройство ПЛК 11: Длина данных (входы)  
585 |  P_ARTICLE_PLCGROUP_INDEXINFILE_11 | Текст |  |  | Подустройство ПЛК 11: описание устройства: индекс в файле  
586 |  P_ARTICLE_PLCDEVICENAME_11 | Текст |  |  | Подустройство ПЛК 11: Имя  
587 |  P_ARTICLE_PLCGROUP_TYPIDENTIFIER_11 | Текст |  |  | Подустройство ПЛК 11: обозначение типа ПЛК  
588 |  P_ARTICLE_PLCDEVICENUMBER_12 | Текст |  |  | Подустройство ПЛК 12: На позиции / разъем  
589 |  P_ARTICLE_PLCGROUP_DATALENGTH_OUTPUTS_12 | Текст |  |  | Подустройство ПЛК 12: Длина данных (выходы)  
590 |  P_ARTICLE_PLCGROUP_DATALENGTH_INPUTS_12 | Текст |  |  | Подустройство ПЛК 12: Длина данных (входы)  
591 |  P_ARTICLE_PLCGROUP_INDEXINFILE_12 | Текст |  |  | Подустройство ПЛК 12: описание устройства: индекс в файле  
592 |  P_ARTICLE_PLCDEVICENAME_12 | Текст |  |  | Подустройство ПЛК 12: Имя  
593 |  P_ARTICLE_PLCGROUP_TYPIDENTIFIER_12 | Текст |  |  | Подустройство ПЛК 12: обозначение типа ПЛК  
594 |  P_ARTICLE_BARDISTANCE | Double |  |  | Сборные шины: Интервал шин  
595 |  P_ARTICLE_BARMOUNTINGPLATEDISTANCE | Double |  |  | Сборные шины: Интервал между шинами и монтажной платой  
596 |  P_ARTICLE_BARCOUNT | Long |  |  | Сборные шины: Число шин  
597 |  P_ARTICLE_BUSBARRAILPARTNR | Текст |  |  | Сборные шины: Номер изделия  
598 |  P_ARTICLE_BUSBARRAILVARIANT | Текст |  |  | Сборные шины: Вариант изделия  
599 |  P_ARTICLE_BARGEOMETRY | Текст |  |  | Сборные шины: Геометрия профиля Г x В (только Eplan Cabinet)  
600 |  P_ARTICLE_BUSBARHOLDERPARTNR | Текст |  |  | Кронштейн сборной шины: Номер изделия  
601 |  P_ARTICLE_BUSBARHOLDERVARIANT | Текст |  |  | Кронштейн сборной шины: Вариант изделия  
602 |  P_ARTICLE_INSERTPOINTOFFSETX | Double |  |  | Кронштейн сборной шины: Вертик. смещение  
603 |  P_ARTICLE_SOUND_PRESSURE_LEVEL_ACCORDING_TO_ISO_20145 | Текст (значение с единицей измерения) | Звуковое давление | dB(A) | Уровень звукового давления в соответствии с ISO 20145  
604 |  P_ARTICLE_SOUND_INSULATION | Текст (значение с единицей измерения) | Звуковое давление | dB | Звукозащита  
605 |  P_ARTICLE_SWITCHING_FREQUENCY | Текст (значение с единицей измерения) | Частота вращения | /h | Частота переключения  
606 |  P_ARTICLE_SWITCHING_CAPACITY | Текст (значение с единицей измерения) | Мощность | Вт | Заряд переключения  
607 |  P_ARTICLE_GROUPSYMBOLMACRO | Текст |  |  | Макрос схемы соединений  
608 |  P_ARTICLE_GROUPSYMBOLMACRO_GB_CCC | Текст |  |  | Макрос схемы соединений: GB/CCC  
609 |  P_ARTICLE_GROUPSYMBOLMACRO_GOST | Текст |  |  | Макрос схемы соединений: ГОСТ  
610 |  P_ARTICLE_GROUPSYMBOLMACRO_IEC | Текст |  |  | Макрос схемы соединений: IEC  
611 |  P_ARTICLE_GROUPSYMBOLMACRO_CUSTOM_MACRO_#index | Текст |  |  | Макрос схемы соединений: Макрос стандарта компании  
612 |  P_ARTICLE_GROUPSYMBOLMACRO_NFPA_INCH | Текст |  |  | Макрос схемы соединений: NFPA дюйм  
613 |  P_ARTICLE_GROUPSYMBOLMACRO_NFPA_MM | Текст |  |  | Макрос схемы соединений: NFPA мм  
614 |  P_ARTICLE_GROUPSYMBOLMACRO_CUSTOM_NAME_#index | Текст |  |  | Макрос схемы соединений: Имя стандарта компании  
615 |  P_ARTICLE_SWITCHING_CURRENT_RESISTIVE_LOAD | Текст (значение с единицей измерения) | Сила электрического тока | A | Ток переключения (омическая нагрузка)  
616 |  P_ARTICLE_TYPE_OF_SWITCHING | Текст (многоязычный) |  |  | Вид переключения  
617 |  P_ARTICLE_APPARENT_POWER | Текст (значение с единицей измерения) | Мощность | V*A | Полная мощность  
618 |  P_ARTICLE_RAILCROSSSECTION | Double |  |  | Поперечное сечение шины  
619 |  P_ARTICLE_RAILMATERIAL | Long |  |  | Материал шины  
620 |  P_ARTICLE_CLOSING_PRESSURE | Текст (значение с единицей измерения) | Давление | kPa | Давление закрытия  
621 |  P_ARTICLE_SLOT_GAP | Double |  |  | Шаг перфорации  
622 |  P_ARTICLE_MAINTENANCE | Текст |  |  | Смазка / техобслуживание  
623 |  P_ARTICLE_PROTECTION_CLASS_IP | Текст |  |  | Степень защиты (IP)  
624 |  P_ARTICLE_PROTECTION_CLASS_IP_OF_THE_EVALUATION_ELECTRONICS | Текст |  |  | Степень защиты (IP): Электронные схемы анализатора  
625 |  P_ARTICLE_PROTECTION_CLASS_IP_FRONT_SIDE | Текст |  |  | Степень защиты (IP): На передней панели  
626 |  P_ARTICLE_PROTECTION_CLASS_IP_OF_THE_MEASURING_HEAD | Текст |  |  | Степень защиты (IP): Измерительная головка  
627 |  P_ARTICLE_PROTECTION_CLASS_IP_MOUNTED | Текст |  |  | Степень защиты (IP): Смонтированный  
628 |  P_ARTICLE_PROTECTION_CLASS_IP_REAR | Текст |  |  | Степень защиты (IP): На задней панели  
629 |  P_ARTICLE_PROTECTION_CLASS_OF_THE_ELECTRIC_MOTOR | Текст |  |  | Класс защиты (двигатель)  
630 |  P_ARTICLE_TARGET_TOTAL_VOLUMETRIC_FLOW | Текст (значение с единицей измерения) | Объемный поток | m³/h | Целевой общий объемный поток  
631 |  P_ARTICLE_TARGET_TOTAL_VOLUMETRIC_FLOW_MAX | Текст (значение с единицей измерения) | Объемный поток | m³/h | Целевой общий объемный поток, макс.  
632 |  P_ARTICLE_TARGET_TOTAL_VOLUMETRIC_FLOW_MIN | Текст (значение с единицей измерения) | Объемный поток | m³/h | Целевой общий объемный поток, мин.  
633 |  P_ARTICLE_SETPOINT_POWER_HYDRAULIC | Текст (значение с единицей измерения) | Мощность | kW | Целевая мощность (гидравлическая)  
634 |  P_ARTICLE_SETPOINT_OUTPUT_HYDRAULIC_MAX | Текст (значение с единицей измерения) | Мощность | kW | Целевая мощность (гидравлическая), макс.  
635 |  P_ARTICLE_SETPOINT_OUTPUT_HYDRAULIC_MIN | Текст (значение с единицей измерения) | Мощность | kW | Целевая мощность (гидравлическая), мин.  
636 |  P_ARTICLE_SETPOINT_OUTPUT_PNEUMATIC | Текст (значение с единицей измерения) | Мощность | kW | Целевая мощность (пневматическая)  
637 |  P_ARTICLE_TARGET_OUTPUT_PNEUMATIC_MAX | Текст (значение с единицей измерения) | Мощность | kW | Целевая мощность (пневматическая), макс.  
638 |  P_ARTICLE_SETPOINT_POWER_PNEUMATIC_MIN | Текст (значение с единицей измерения) | Мощность | kW | Целевая мощность (пневматическая), мин.  
639 |  P_ARTICLE_SET_POINT | Текст (значение с единицей измерения) |  |  | Целевое значение  
640 |  P_ARTICLE_VOLTAGE_LOAD_RESISTIVE_LOAD_DC_MAX | Текст (значение с единицей измерения) | Электрическое напряжение | V | Нагрузка по напряжению (омическая нагрузка, постоянный ток), макс.  
641 |  P_ARTICLE_HEAT_OUTPUT_SPECIFIC | Текст (значение с единицей измерения) | Теплопроводность | W/K | Указанная тепловая мощность  
642 |  P_ARTICLE_PLUG_TYPE | Текст (многоязычный) |  |  | Тип штекера  
643 |  P_ARTICLE_PLUG_CONNECTOR_CONNECTION_1 | Текст (многоязычный) |  |  | Штекерный разъем (вывод устройства 1)  
644 |  P_ARTICLE_PLUG_CONNECTOR_CONNECTION_2 | Текст (многоязычный) |  |  | Штекерный разъем (вывод устройства 2)  
645 |  P_ARTICLE_CONNECTOR_DESIGN | Текст (многоязычный) |  |  | Исполнение штекерного разъема  
646 |  P_ARTICLE_CONNECTOR_HOUSING_OF_CONNECTION_1 | Текст (многоязычный) |  |  | Корпус штекерного разъема (вывод устройства 1)  
647 |  P_ARTICLE_CONNECTOR_HOUSING_OF_THE_CONNECTION_2 | Текст (многоязычный) |  |  | Корпус штекерного разъема (вывод устройства 2)  
648 |  P_ARTICLE_TAB_WIDTH | Double |  |  | Ширина зуба  
649 |  P_ARTICLE_CONTROL_SIGNAL_TYPE | Текст (многоязычный) |  |  | Управляющий сигнал: Тип  
650 |  P_ARTICLE_CONTROL_PRESSURE_MAX | Текст (значение с единицей измерения) | Давление | бар | Вспомогательное давление, макс.  
651 |  P_ARTICLE_CONTROL_PRESSURE_MIN | Текст (значение с единицей измерения) | Давление | бар | Вспомогательное давление, мин.  
652 |  P_ARTICLE_CONTROL_FLOW_RATE | Текст (значение с единицей измерения) | Объемный поток | m³/h | Объемный поток управления  
653 |  P_ARTICLE_SHOCK_LOAD | Текст (значение с единицей измерения) | Сила электрического тока | A | Ударная нагрузка  
654 |  P_PART_ADDRESS_STREET | Текст |  |  | Улица  
655 |  P_ARTICLE_IDENTCODE | Текст |  |  | Номер штрих-кода  
656 |  P_ARTICLE_IDENTTYPE | Текст |  |  | Тип штрих-кода  
657 |  P_ARTICLE_CURRENT_CONSUMPTION | Текст (значение с единицей измерения) | Сила электрического тока | A | Потребление тока  
658 |  P_ARTICLE_CURRENT_CONSUMPTION_MAX | Текст (значение с единицей измерения) | Сила электрического тока | A | Потребление тока, макс.  
659 |  P_ARTICLE_CURRENT_CARRYING_CAPACITY | Текст (значение с единицей измерения) | Сила электрического тока | A | Способность выдерживать токовую нагрузку  
660 |  P_ARTICLE_CURRENT_LOAD_RESISTIVE_LOAD_DC_MAX | Текст (значение с единицей измерения) | Сила электрического тока | A | Способность выдерживать токовую нагрузку (омическая нагрузка, постоянный ток), макс.  
661 |  P_ARTICLE_CURRENT_CARRYING_CAPACITY_MAX_PER_CONNECTION_SOCKET | Текст (значение с единицей измерения) | Сила электрического тока | A | Способность выдерживать токовую нагрузку (на одно соединительное гнездо), макс.  
662 |  P_ARTICLE_CURRENT_CARRYING_CAPACITY_MAX_PER_I_O_SIGNAL | Текст (значение с единицей измерения) | Сила электрического тока | A | Способность выдерживать токовую нагрузку (на сигнал В/В), макс.  
663 |  P_ARTICLE_FUSE_PROTECTION_ON_SITE | Текст (многоязычный) |  |  | Сила тока (защита на рабочем месте)  
664 |  P_ARTICLE_REPORT_SYMBOL_#index | Текст |  |  | Символ отчета  
665 |  P_ARTICLE_NUMBER_OF_TCF_METHODS | Текст (значение с единицей измерения) | Количество | Stück | TCF: Количество методов вычисления  
666 |  P_ARTICLE_TCF_TRANSPORT_CARBON_FOOTPRINT_CALCULATION | Текст (значение с единицей измерения) |  |  | TCF: Вычисление  
667 |  P_ARTICLE_TCF_CALCULATION_METHOD | Текст (значение с единицей измерения) |  |  | TCF: Метод вычисления  
668 |  P_ARTICLE_TCF_REFERENCE_VALUE_FOR_CALCULATION | Текст (значение с единицей измерения) |  |  | TCF: Базовый параметр для вычисления  
669 |  P_ARTICLE_TCF_CO2EQ | Текст (значение с единицей измерения) |  |  | TCF: Эквивалент CO2  
670 |  P_ARTICLE_TCF_QUANTITY_REFERENCE_FOR_CALCULATION | Текст (значение с единицей измерения) |  |  | TCF: Указание количества для вычисления  
671 |  P_ARTICLE_TCF_PROCESSES_FOR_GREENHOUSE_GAS_EMISSIONS_FOR_A_TRANSPORT_SERVICE | Текст (значение с единицей измерения) |  |  | TCF: Процессы выбросов парниковых газов для транспортной услуги  
672 |  P_ARTICLE_TCF_GOODS_HANDOVER_ADDRESS | Текст (значение с единицей измерения) |  |  | TCF: Адрес передачи товара  
673 |  P_ARTICLE_TCF_GOODS_ACCEPTANCE_ADDRESS | Текст (значение с единицей измерения) |  |  | TCF: Адрес получения товара  
674 |  P_ARTICLE_PIECETYPE | Текст |  |  | Вид изделия  
675 |  P_ARTICLE_PARTIAL_LENGTH | Текст (значение с единицей измерения) |  |  | Подмножество / длина  
676 |  P_PART_ADDRESS_PHONE | Текст |  |  | Телефон  
677 |  P_ARTICLE_TEMPERATUR_MEDIUM_MAX | Текст (значение с единицей измерения) | Температура | °C | Температура (среда), макс.  
678 |  P_ARTICLE_TEMPERATUR_MEDIUM_MIN | Текст (значение с единицей измерения) | Температура | °C | Температура (среда), мин.  
679 |  P_ARTICLE_TEMPERATURE_MAX | Текст (значение с единицей измерения) | Температура | °C | Температура, макс.  
680 |  P_ARTICLE_TEMPERATURE_MIN | Текст (значение с единицей измерения) | Температура | °C | Температура, мин.  
681 |  P_ARTICLE_TEMPERATURE_RANGE_MEDIUM_MAX | Текст (значение с единицей измерения) | Температура | °C | Диапазон температур (среда), макс.  
682 |  P_ARTICLE_TEMPERATURE_RANGE_MEDIUM_MIN | Текст (значение с единицей измерения) | Температура | °C | Диапазон температур (среда), мин.  
683 |  P_ARTICLE_TEMPERATURE_COEFFICIENT | Текст |  |  | Температурный коэффициент  
684 |  P_ARTICLE_ECABINET_MACRO | Текст |  |  | текстура  
685 |  P_ARTICLE_DEPTH | Double |  |  | Глубина  
686 |  P_ARTICLE_BOTTOMPANELDEPTH | Double |  |  | Глубина пола  
687 |  P_ARTICLE_TOPPANELDPEPTH | Double |  |  | Глубина крыши  
688 |  P_ARTICLE_PROFILEDEPTH | Double |  |  | Глубина профиля, поперек  
689 |  P_ARTICLE_VPROFILEDPETH | Double |  |  | Глубина профиля, вертик.  
690 |  P_ARTICLE_REARPANELDPEPTH | Double |  |  | Глубина задней стенки  
691 |  P_ARTICLE_SIDEPANELDEPTH | Double |  |  | Глубина боковой стенки  
692 |  P_ARTICLE_TYPENR | Текст |  |  | Номер типа  
693 |  P_ARTICLE_HINGEPOSITION | Long (список выбора) |  |  | Дверь: Шарнир  
694 |  P_ARTICLE_DOORTYPE | Текст |  |  | Дверь: Тип  
695 |  P_ARTICLE_DOORTHICKNESS | Double |  |  | Дверь: Толщина стенки  
696 |  P_ARTICLE_DOOR_RABBET | Double |  |  | Фальц двери  
697 |  P_ARTICLE_DOOR_OFFSET_TOP | Double |  |  | Дверной проем: Смещение вверху  
698 |  P_ARTICLE_DOOR_OFFSET_RIGHT | Double |  |  | Дверной проем: Смещение справа  
699 |  P_ARTICLE_MAX_AMBIENT_TEMPERATURE_DURING_OPERATION | Текст (значение с единицей измерения) | Температура | °C | Температура окружающей среды (во время эксплуатации), макс.  
700 |  P_ARTICLE_MIN_AMBIENT_TEMPERATURE_DURING_OPERATION | Текст (значение с единицей измерения) | Температура | °C | Температура окружающей среды (во время эксплуатации), мин.  
701 |  P_ARTICLE_SUBCRAFT_ELECTRICAL_#index | Текст (многоязычный) |  |  | Подраздел 'Электротехника'  
702 |  P_ARTICLE_SUBCRAFT_FLUID_UNDEFINED_#index | Текст (многоязычный) |  |  | Подраздел 'Fluid (не определен)'  
703 |  P_ARTICLE_SUBCRAFT_GASTECHNOLOGY_#index | Текст (многоязычный) |  |  | Подраздел 'Газовая техника'  
704 |  P_ARTICLE_SUBCRAFT_HYDRAULICS_#index | Текст (многоязычный) |  |  | Подраздел 'Гидравлика'  
705 |  P_ARTICLE_SUBCRAFT_COOLINGLUBRICANT_#index | Текст (многоязычный) |  |  | Подраздел 'Смазочно-охлаждающая жидкость'  
706 |  P_ARTICLE_SUBCRAFT_COOLING_#index | Текст (многоязычный) |  |  | Подраздел 'Охлаждение'  
707 |  P_ARTICLE_SUBCRAFT_MECHANICS_#index | Текст (многоязычный) |  |  | Подраздел 'Механика'  
708 |  P_ARTICLE_SUBCRAFT_PNEUMATICS_#index | Текст (многоязычный) |  |  | Подраздел 'Пневматика'  
709 |  P_ARTICLE_SUBCRAFT_LUBRICATION_#index | Текст (многоязычный) |  |  | Подраздел 'Смазка'  
710 |  P_ARTICLE_SUBCRAFT_PROCESS_#index | Текст (многоязычный) |  |  | Подраздел 'Технология производственных процессов'  
711 |  P_PART_TERMINAL_TYPEDEFAULT | Long |  |  | Обработка концов проводов (Eplan Cabinet, станд.)  
712 |  P_ARTICLE_SALESPRICE_1 | Double |  |  | Продажная цена Валюта 1  
713 |  P_ARTICLE_SALESPRICE_2 | Double |  |  | Продажная цена Валюта 2  
714 |  P_PART_TERMINAL_DIRECTION | Long (список выбора) |  |  | Направление подсоединения (стандарт)  
715 |  P_ARTICLE_POWER_LOSS_PER_POLE_CURRENT_DEPENDENT_PVIP | Текст (значение с единицей измерения) | Мощность | Вт | Мощность потерь (на полюс), зависит от тока  
716 |  P_ARTICLE_POWER_LOSS_STATIC_CURRENT_INDEPENDENT_PVS | Текст (значение с единицей измерения) | Мощность | Вт | Мощность потерь (статическая), не зависит от тока  
717 |  P_ARTICLE_ACTIVE_POWER_LOSS | Текст (значение с единицей измерения) | Мощность | Вт | Мощность потерь  
718 |  P_ARTICLE_WEAR | Текст |  |  | Изнашиваемая деталь  
719 |  P_ARTICLE_SUPPLY_VOLTAGE | Текст (значение с единицей измерения) | Электрическое напряжение | V | Напряжение питания  
720 |  P_ARTICLE_SUPPLY_VOLTAGE_AT_AC_50_HZ | Текст (значение с единицей измерения) | Электрическое напряжение | V | Напряжение питания (при переменном токе 50 Гц)  
721 |  P_ARTICLE_SUPPLY_VOLTAGE_AT_AC_50_HZ_MAX | Текст (значение с единицей измерения) | Электрическое напряжение | V | Напряжение питания (при переменном токе 50 Гц), макс.  
722 |  P_ARTICLE_SUPPLY_VOLTAGE_AT_AC_50_HZ_MIN | Текст (значение с единицей измерения) | Электрическое напряжение | V | Напряжение питания (при переменном токе 50 Гц), мин.  
723 |  P_ARTICLE_SUPPLY_VOLTAGE_AT_AC_60_HZ | Текст (значение с единицей измерения) | Электрическое напряжение | V | Напряжение питания (при переменном токе 60 Гц)  
724 |  P_ARTICLE_SUPPLY_VOLTAGE_AT_AC_60_HZ_MAX | Текст (значение с единицей измерения) | Электрическое напряжение | V | Напряжение питания (при переменном токе 60 Гц), макс.  
725 |  P_ARTICLE_SUPPLY_VOLTAGE_AT_AC_60_HZ_MIN | Текст (значение с единицей измерения) | Электрическое напряжение | V | Напряжение питания (при переменном токе 60 Гц), мин.  
726 |  P_ARTICLE_SUPPLY_VOLTAGE_FOR_DC | Текст (значение с единицей измерения) | Электрическое напряжение | V | Напряжение питания (при постоянном токе)  
727 |  P_ARTICLE_SUPPLY_VOLTAGE_FOR_DC_MAX | Текст (значение с единицей измерения) | Электрическое напряжение | V | Напряжение питания (при постоянном токе), макс.  
728 |  P_ARTICLE_SUPPLY_VOLTAGE_FOR_DC_MIN | Текст (значение с единицей измерения) | Электрическое напряжение | V | Напряжение питания (при постоянном токе), мин.  
729 |  P_ARTICLE_SUPPLY_VOLTAGE_ADJUSTABLE | Текст (значение с единицей измерения) | Электрическое напряжение | V | Напряжение питания с возможностью регулирования  
730 |  P_ARTICLE_SUPPLY_VOLTAGE_MAX | Текст (значение с единицей измерения) | Электрическое напряжение | V | Напряжение питания, макс.  
731 |  P_ARTICLE_SUPPLY_VOLTAGE_MIN | Текст (значение с единицей измерения) | Электрическое напряжение | V | Напряжение питания, мин.  
732 |  P_ARTICLE_SUPPLY_VOLTAGE_RANGE | Текст (значение с единицей измерения) | Электрическое напряжение | V | Диапазон напряжения питания  
733 |  P_ARTICLE_USE_FOR_MARKING_TYPE | Текст (многоязычный) |  |  | Использование для типа маркировки  
734 |  P_ARTICLE_VISCOSITY | Текст (значение с единицей измерения) | Динамическая вязкость | kg/m*s | Вязкость  
735 |  P_ARTICLE_VISCOSITY_INDEX_ACCORDING_TO_DIN_ISO_2909 | Текст (значение с единицей измерения) |  |  | Индекс вязкости (согласно DIN ISO 2909)  
736 |  P_ARTICLE_VISCOSITY_CLASS_ACCORDING_TO_DIN_51519 | Текст (значение с единицей измерения) |  |  | Класс вязкости (согласно DIN 51519)  
737 |  P_ARTICLE_VOLUME | Текст (значение с единицей измерения) | Масса на объем | kg/m³ | Объем  
738 |  P_ARTICLE_VOLUME_FLOW_HEATING_M3_H | Текст (значение с единицей измерения) | Объемный поток | m³/h | Объемный поток  
739 |  P_ARTICLE_VOLUME_FLOW_FREELY_BLOWING | Текст (значение с единицей измерения) | Объемный поток | m³/h | Объемный поток (продувка)  
740 |  P_ARTICLE_VOLUME_FLOW_MAX_M3_H | Текст (значение с единицей измерения) | Объемный поток | m³/h | Объемный поток (в м³/ч), макс.  
741 |  P_ARTICLE_WALLTHICKNESS | Double |  |  | Толщина стенки  
742 |  P_ARTICLE_MAINTENANCE_INTERVAL | Текст (многоязычный) |  |  | Интервал технического обслуживания  
743 |  P_ARTICLE_MAINTENANCE_CYCLE | Текст (многоязычный) |  |  | Цикл технического обслуживания  
744 |  P_ARTICLE_SEALING_MATERIAL | Текст (многоязычный) |  |  | Материал уплотнения  
745 |  P_ARTICLE_MATERIAL_OF_THE_CABLE_INNER_CONDUCTOR | Текст (многоязычный) |  |  | Материал внутреннего проводника кабеля  
746 |  P_ARTICLE_MATERIAL_OF_THE_CABLE_SHEATH | Текст (многоязычный) |  |  | Материал оболочки кабеля  
747 |  P_ARTICLE_MATERIAL_LIST | Long |  |  | Список выбора материала  
748 |  P_ARTICLE_ACTIVE_POWER | Текст (значение с единицей измерения) | Мощность | Вт | Активная мощность  
749 |  P_ARTICLE_ACTIVE_POWER_MAX_ASV | Текст (значение с единицей измерения) | Мощность | Вт | Активная мощность (общий источник питания), макс.  
750 |  P_ARTICLE_ACTIVE_POWER_MAX_NEA | Текст (значение с единицей измерения) | Мощность | Вт | Активная мощность (установка резервного питания), макс.  
751 |  P_ARTICLE_ACTIVE_POWER_MAX_UPS | Текст (значение с единицей измерения) | Мощность | Вт | Активная мощность (источник бесперебойного питания), макс.  
752 |  P_ARTICLE_EFFICIENCY | Текст (значение с единицей измерения) | Процент | % | КПД  
753 |  P_PART_ADDRESS_TOWN | Текст |  |  | Место жительства  
754 |  P_ARTICLE_CERTIFICATE_ATEX | Текст |  |  | Сертификация: Идентификатор ATEX  
755 |  P_ARTICLE_CERTIFICATE | Текст |  |  | Сертификация: общ.  
756 |  P_ARTICLE_CERTIFICATE_CE | Булево (истина/ложь) |  |  | Сертификац.: ид. CE  
757 |  P_ARTICLE_CERTIFICATE_UL | Текст |  |  | Сертификация: UL File Number  
758 |  P_ARTICLE_CERTIFICATE_VDE | Текст |  |  | Сертификация: ид. VDE  
759 |  P_ARTICLE_ACCESSORYID | Текст |  |  | Ид. принадлежн.  
760 |  P_ARTICLEACCESSORYLIST_INSERT_COMPLETE | Булево (истина/ложь) |  |  | Вставить полностью список принадлежностей  
761 |  P_ARTICLE_PERMISSIBLE_EXTERNAL_CABLE_TEMPERATURE_FIXED_INSTALLATION_MAX | Текст (значение с единицей измерения) | Температура | °C | Допустимая внешняя температура кабеля (стационарно проложенного), макс.  
762 |  P_ARTICLE_PERMISSIBLE_EXTERNAL_CABLE_TEMPERATURE_IN_MOTION_MAX | Текст (значение с единицей измерения) | Температура | °C | Допустимая внешняя температура кабеля (в движении), макс.  
763 |  P_ARTICLE_PERMISSIBLE_SURFACE_TEMPERATURE_WITH_MOVING_CONDUCTOR_MAX | Текст (значение с единицей измерения) | Температура | °C | Допустимая температура поверхности (с движущимся проводником), макс.  
764 |  P_ARTICLE_PERMISSIBLE_SURFACE_TEMPERATURE_WITH_FIXED_CONDUCTOR_MAX | Текст (значение с единицей измерения) | Температура | °C | Допустимая температура поверхности (со стационарно проложенным проводником), макс.  
765 |  P_ARTICLE_PERMISSIBLE_BENDING_RADIUS_FLEXIBLE_USE_FREE_MOVEMENT_MIN | Текст (многоязычный) |  |  | Допустимый радиус изгиба (гибкое использование со свободным перемещением), мин.  
766 |  P_ARTICLE_PERMISSIBLE_BENDING_RADIUS_FLEXIBLE_USE_WITH_FORCED_GUIDANCE_MIN | Текст (многоязычный) |  |  | Допустимый радиус изгиба (гибкое использование с принудительной подачей), мин.  
767 |  P_ARTICLE_PERMISSIBLE_BENDING_RADIUS_STATIONARY_USE_FIXED_INSTALLATION_MIN | Текст (многоязычный) |  |  | Допустимый радиус изгиба (стационарное использование с неподвижным монтажом), мин.  
768 |  P_PART_TERMINAL_ADDITIONALLENGTHDEFAULT | Double |  |  | Дополнительная длина (стандарт)  
769 |  P_PART_LASTCHANGE_DATE_UTC | Целое число (время) |  |  | Дата изменения (UTC)  
770 |  P_ARTICLE_OPENING_PRESSURE | Текст (значение с единицей измерения) | Давление | бар | Давление открытия  
771 |  P_ARTICLE_OVERLOAD_CAPACITY_OVERCURRENT | Текст (значение с единицей измерения) | Сила электрического тока | A | Перегрузочная способность: Ток перегрузки  
772 |  P_ARTICLE_BOTTOMPANELPROJECTIONBACK | Double |  |  | Выступ пола сзади  
773 |  P_ARTICLE_BOTTOMPANELPROJECTIONLEFT | Double |  |  | Выступ пола слева  
774 |  P_ARTICLE_BOTTOMPANELPROJECTIONRIGHT | Double |  |  | Выступ пола справа  
775 |  P_ARTICLE_BOTTOMPANELPROJECTIONFRONT | Double |  |  | Выступ пола спереди  
776 |  P_ARTICLE_TOPPANELPROJECTIONBACK | Double |  |  | Выступ крыши сзади  
777 |  P_ARTICLE_TOPPANELPROJECTIONLEFT | Double |  |  | Выступ крыши слева  
778 |  P_ARTICLE_TOPPANELPROJECTIONRIGHT | Double |  |  | Выступ крыши справа  
779 |  P_ARTICLE_TOPPANELPROJECTIONFRONT | Double |  |  | Выступ крыши спереди  
780 |  P_ARTICLE_REARPANELPROJECTIONLEFT | Double |  |  | Выступ задней стенки слева  
781 |  P_ARTICLE_REARPANELPROJECTIONTOP | Double |  |  | Выступ задней стенки сверху  
782 |  P_ARTICLE_REARPANELPROJECTIONRIGHT | Double |  |  | Выступ задней стенки справа  
783 |  P_ARTICLE_REARPANELPROJECTIONBOTTOM | Double |  |  | Выступ задней стенки снизу  
784 |  P_ARTICLE_SIDEPANELPROJECTIONBACK | Double |  |  | Выступ боковой стенки сзади  
785 |  P_ARTICLE_SIDEPANELPROJECTIONTOP | Double |  |  | Выступ боковой стенки сверху  
786 |  P_ARTICLE_SIDEPANELPROJECTIONBOTTOM | Double |  |  | Выступ боковой стенки снизу  
787 |  P_ARTICLE_SIDEPANELPROJECTIONFRONT | Double |  |  | Выступ боковой стенки спереди  

### Свойства изделия <variant>

**№** | **Атрибут** | **Тип** | **Группа** | **Единица измерения** | **Свойство**  
---|---|---|---|---|---  
1 |  P_ARTICLE_ADDRESSRANGE_2 | Текст |  |  | Диапазон адресов 2 (SIEMENS STEP 7 Classic)  
2 |  P_ARTICLE_ADDRESSRANGE | Текст |  |  | Диапазон адресов (SIEMENS STEP 7 Classic)  
3 |  P_ARTICLE_CONNECTION | Текст |  |  | Вывод устройства  
4 |  P_ARTICLE_TERMINALSIZE_SOURCE | Текст (значение с единицей измерения) |  |  | Размер присоединения, источник  
5 |  P_ARTICLE_TERMINALSIZE_DESTINATION | Текст (значение с единицей измерения) |  |  | Размер присоединения, цель  
6 |  P_ARTICLE_CONNECTIONCROSSSECTION | Текст (значение с единицей измерения) |  |  | Сечение вывода устройства  
7 |  P_ARTICLE_PLCAXIS_DEVICETYPE | Текст |  |  | Привод: тип устройства  
8 |  P_ARTICLE_TRIGGERCURRENT | Текст (значение с единицей измерения) | Сила электрического тока |  A* | Ток расцепления  
9 |  P_ARTICLE_OUTERDIAMETER | Текст (значение с единицей измерения) | Длина | мм | Внешний диаметр  
10 |  P_ARTICLE_ASSEMBLY_POS_PLACE_SPREADED | Булево (истина/ложь) |  |  | Распределенное размещение узла  
11 |  P_ARTICLE_PLCISBUSCOUPLER | Булево (истина/ложь) |  |  | Шинный интерфейс / первичная станция  
12 |  P_ARTICLE_PLCISBUSDISTRIBUTOR | Булево (истина/ложь) |  |  | Шинный ответвитель  
13 |  P_ARTICLE_PLCISCPU | Булево (истина/ложь) |  |  | ЦПУ  
14 |  P_ARTICLE_FLOW | Double |  |  | Расход  
15 |  P_ARTICLE_INTRINSICSAFETY | Булево (истина/ложь) |  |  | Искробезопасн.  
16 |  P_ARTICLE_WIRECROSSSECTION_UNIT | Long (список выбора) |  |  | Единица измерения поперечного сечения / диаметра соединения  
17 |  P_ARTICLE_COLOR | Текст (многоязычный) |  |  | Цвет  
18 |  P_ARTICLE_FLUID_WALLTHICKNESS | Текст (значение с единицей измерения) | Длина |  m* | Fluid-техника / технология производственных процессов: Толщина стенки соединения  
19 |  P_ARTICLE_PLCDEVICE_ID | Текст |  |  | Описание устройства: Имя файла  
20 |  P_ARTICLE_PLCDEVICE_INDEX | Текст |  |  | Описание устройства: Индекс в файле  
21 |  P_ARTICLE_CABLEWEIGHT | Текст (значение с единицей измерения) | Масса на длину | kg/km | Вес/длина  
22 |  P_ARTICLE_THREAD | Текст |  |  | Резьба  
23 |  P_ARTICLE_HOLDINGPOWER | Текст (значение с единицей измерения) | Мощность | mW | Мощность на удержание  
24 |  P_ARTICLE_STROKELENGTH | Текст (значение с единицей измерения) | Длина | мм | Длина хода  
25 |  P_ARTICLE_INNERDIAMETER | Текст (значение с единицей измерения) | Длина | мм | Внутр. диаметр  
26 |  P_ARTICLE_CABLEDESIGNATION | Текст (многоязычный) |  |  | Кабель / Группа соединений: Обозначение в графике  
27 |  P_ARTICLE_CABLEDISPLAYFORM | Текст |  |  | Форма схемы кабельных соединений  
28 |  P_ARTICLE_CABLETYPE | Текст |  |  | Тип кабеля / обозначение типа  
29 |  P_ARTICLE_AWGTILL | Текст |  |  | Клеммы: AWG до  
30 |  P_ARTICLE_AWGFROM | Текст |  |  | Клеммы: AWG от  
31 |  P_ARTICLE_CROSSSECTIONTILL | Текст (значение с единицей измерения) | Площадь | мм² | Клеммы: сечение до  
32 |  P_ARTICLE_CROSSSECTIONFROM | Текст (значение с единицей измерения) | Площадь | мм² | Клеммы: сечение от  
33 |  P_ARTICLE_DEGOFPROTECTION | Текст (многоязычный) |  |  | Клеммы: Степень защиты  
34 |  P_ARTICLE_VOLTAGECSA | Текст (значение с единицей измерения) | Электрическое напряжение |  V* | Клеммы: напряжение CSA  
35 |  P_ARTICLE_VOLTAGEIEC | Текст (значение с единицей измерения) | Электрическое напряжение |  V* | Клеммы: напряжение IEC  
36 |  P_ARTICLE_VOLTAGEUL | Текст (значение с единицей измерения) | Электрическое напряжение |  V* | Клеммы: напряжение UL  
37 |  P_ARTICLE_CURRENTCSA | Текст (значение с единицей измерения) | Сила электрического тока |  A* | Клеммы: ток CSA  
38 |  P_ARTICLE_CURRENTIEC | Текст (значение с единицей измерения) | Сила электрического тока |  A* | Клеммы: ток IEC  
39 |  P_ARTICLE_CURRENTUL | Текст (значение с единицей измерения) | Сила электрического тока |  A* | Клеммы: ток UL  
40 |  P_ARTICLE_COPPERNUMBER | Текст (значение с единицей измерения) |  |  | Удельный вес по меди  
41 |  P_ARTICLE_SHORTCIRCUITRESISTANT | Булево (истина/ложь) |  |  | Устойчивый к коротким замыканиям  
42 |  P_ARTICLE_CABLELENGTH | Double |  |  | Длина (в предварительно собранном виде)  
43 |  P_ARTICLE_PRESSURE | Double |  |  | Макс. рабочее давление  
44 |  P_ARTICLE_POWERDISSIPATION | Текст (значение с единицей измерения) | Мощность | Вт | Макс. мощность потерь  
45 |  P_ARTICLE_BENDINGRADIUS | Текст (значение с единицей измерения) | Длина | мм | Мин. радиус изгиба  
46 |  P_ARTICLE_MODULE_POS_PLACE_SPREADED | Long |  |  | Распределенное размещение модуля  
47 |  P_ARTICLE_PANELWIDTH | Double |  |  | Монтажная плата: Оснащаемая ширина  
48 |  P_ARTICLE_PANELHEIGHT | Double |  |  | Монтажная плата: Оснащаемая высота  
49 |  P_ARTICLE_PANELDEPTH | Double |  |  | Монтажная плата: Максимальная глубина установки  
50 |  P_ARTICLE_PANELMOUNTINGSPACE | Double |  |  | Монтажная плата: Место монтажа  
51 |  P_ARTICLE_PRESSURELEVEL | Текст |  |  | Ступень номинального давления  
52 |  P_ARTICLE_WIDTHRATING | Текст |  |  | Номинальная ширина  
53 |  P_ARTICLE_NORM | Текст |  |  | Стандарт  
54 |  P_ARTICLE_PLCOBJECT_DESCRIPTION | Текст |  |  | Описание объекта  
55 |  P_ARTICLE_ADJUSTRANGE | Double |  |  | Диап. регулир.  
56 |  P_ARTICLE_PIPECLASS | Текст |  |  | Класс трубы  
57 |  P_ARTICLE_PLCTEMPLATEREFERENCE | Текст |  |  | Устройство ПЛК: TemplateIdentifier  
58 |  P_ARTICLE_PLCISMOUNTEDONHEADMODULE | Булево (истина/ложь) |  |  | Карта ПЛК вставлена в первичную станцию  
59 |  P_ARTICLE_PLCSTATIONTYPE | Текст |  |  | Рабочая станция ПЛК: Тип  
60 |  P_ARTICLE_PLCTYPE | Текст |  |  | Обозначение типа ПЛК  
61 |  P_ARTICLE_ELECTRICALPOWER | Текст (значение с единицей измерения) | Мощность | Вт | Коммутационная способность  
62 |  P_ARTICLE_VOLTAGE | Текст (значение с единицей измерения) | Электрическое напряжение |  V* | Напряжение  
63 |  P_ARTICLE_VOLTAGETYPE | Текст |  |  | Вид напряжения  
64 |  P_ARTICLE_PLCISPOWERSUPPLY | Булево (истина/ложь) |  |  | Электропитание  
65 |  P_ARTICLE_COILVOLTAGE | Текст (значение с единицей измерения) | Электрическое напряжение |  V* | Катушка: Напряжение  
66 |  P_ARTICLE_CONTACTOR_ARRANGEMENT | Текст |  |  | Штекеры: Расположение контактов штекера  
67 |  P_ARTICLE_CONNECTIONMETHOD | Текст (многоязычный) |  |  | Штекер: техника вывода устройства  
68 |  P_ARTICLE_PINCOUNT | Текст |  |  | Штекеры: Количество контактов штекера  
69 |  P_ARTICLE_DESIGN | Текст (многоязычный) |  |  | Штекер: конструкция  
70 |  P_ARTICLE_CODING | Текст |  |  | Штекеры: Кодировка  
71 |  P_ARTICLE_CREEPAGEDISTANCE | Текст (значение с единицей измерения) | Длина |  m* | Штекер: путь утечки  
72 |  P_ARTICLE_AIRGAP | Текст (значение с единицей измерения) | Длина |  m* | Штекер: воздушн. интервал  
73 |  P_ARTICLE_STANDARDINVERS | Текст |  |  | Штекер: Станд. / обратн.  
74 |  P_ARTICLE_CONTACTTYPE | Текст (многоязычный) |  |  | Штекеры: Вид контактов штекера  
75 |  P_ARTICLE_ADVANCECONTACTS | Текст |  |  | Штекеры: Опережающие контакты штекера  
76 |  P_ARTICLE_ELECTRICALCURRENT | Текст (значение с единицей измерения) | Сила электрического тока |  A* | Ток  
77 |  P_ARTICLE_CHARACTERISTICS | Текст (значение с единицей измерения) |  |  | Технические параметры  
78 |  P_ARTICLE_DOORWIDTH | Double |  |  | Дверь: оснащаемая ширина  
79 |  P_ARTICLE_DOORHEIGHT | Double |  |  | Дверь: оснащаемая высота  
80 |  P_ARTICLE_DOORDEPTH | Double |  |  | Дверь: макс. глубина установки  
81 |  P_ARTICLE_DOORMOUNTINGSPACE | Double |  |  | Дверь: место монтажа  
82 |  P_ARTICLE_VARIANT | Текст |  |  | Вариант  
83 |  P_ARTICLE_CONNECTION_WIRECROSSSECTION_UNIT | Long |  |  | Соединение: Единица измерения поперечного сечения / диаметра соединения  
84 |  P_ARTICLE_CABLEWIRECOUNT | Текст |  |  | Число соединений  
85 |  P_ARTICLE_WIRECROSSSECTION_AND_DIAMETER | Текст (значение с единицей измерения) |  |  | Число соединений и поперечное сечение / диаметр  
86 |  P_ARTICLE_CABLEWIRECROSSSECTION | Текст (значение с единицей измерения) | Длина |  m* | Поперечное сечение / диаметр соединения  
87 |  P_ARTICLE_WIRETYPE | Текст |  |  | Вид соединения  
88 |  P_ARTICLE_FIRMWAREVERSION | Текст |  |  | Версия  
89 |  P_ARTICLE_MATERIAL | Текст (многоязычный) |  |  | Материал  

###  <freeproperty>

**№** | **Атрибут** | **Тип** | **Свойство**  
---|---|---|---  
1 |  pos | Короткое целое | Индекс свойства (1000)  
2 |  P_ARTICLE_FREE_DATA_DESCRIPTION | Текст (многоязычный) | Произвольные свойства: Отображаемое имя  
3 |  P_ARTICLE_FREE_DATA_VALUE | Текст (многоязычный) | Произв. свойство: Значение  
4 |  P_ARTICLE_FREE_DATA_UNIT | Текст | Произвольн. свойства: Единица измерения  

### <userproperty>

**№** | **Атрибут** | **Тип** | **Свойство**  
---|---|---|---  
1 |  P_ARTICLE_FREE_DATA_IDENTNAME | Текст | Определенные пользователем свойства: Идентифицирующее имя  
2 |  pos | Короткое целое | Индекс свойства (1000)  
3 |  P_ARTICLE_FREE_DATA_NEWVALUE | Текст (многоязычный) | Определенные пользователем свойства: Значение  

###  <constructionPosition>

**№** | **Атрибут** | **Тип** | **Свойство**  
---|---|---|---  
1 |  offsetx | Double | Смещение в направлении X (схема сверления)  
2 |  offsety | Double | Смещение в направлении Y (схема сверления)  
3 |  name | Текст | Имя (схема сверления)  
4 |  pos | Короткое целое | Позиция  

###  <accessoryposition>

**№** | **Атрибут** | **Тип** | **Свойство**  
---|---|---|---  
1 |  necessary | Булево (истина/ложь) | Необходимый  
2 |  partnr | Текст | Номер изделия / имя  
3 |  variant | Текст | Вариант  
4 |  parttype | Long | Тип записи данных  
5 |  placement | Текст | Размещение принадлежностей  
6 |  pos | Короткое целое | Позиция  
7 |  parentvariant | Текст | Вариант узла/модуля  

###  <attributeposition>

**№** | **Атрибут** | **Тип** | **Свойство**  
---|---|---|---  
1 |  pos | Короткое целое | Индекс свойства  
2 |  P_ARTICLE_ATTRIBUTE_VALUE | Текст | Атрибут  

###  <functiontemplate>

**№** | **Атрибут** | **Тип** | **Свойство**  
---|---|---|---  
1 |  functiondefcategory | Короткое целое | Категория (Данные функции)  
2 |  functiondefgroup | Короткое целое | Группа (данные функции)  
3 |  functiondefid | Короткое целое | Определение функции (данные функции)  
4 |  manualmoduletemplate | Булево (истина/ложь) | Flag ManuallySet  
5 |  notallowedasmainfunction | Булево (истина/ложь) | Flag NotAllowedAsMainFunction  
6 |  characteristics | Текст (значение с единицей измерения) | Технические параметры  
7 |  terminalNr | Текст | Обозначение клеммы / контакта штекера  
8 |  description | Текст | Описание клемм / контактов штекера  
9 |  terminalfunction | Long (список выбора) | Категория клеммы  
10 |  hasled | Булево (истина/ложь) | Клемма со светодиодом  
11 |  additionaldescription | Текст (многоязычный) | Описание  
12 |  hasplugadapter | Булево (истина/ложь) | Клемма со штекерным адаптером  
13 |  plcbussystem | Long (список выбора) | Система шин  
14 |  terminallabeltype | Текст | Тип маркировки  
15 |  connectiondimension | Текст (значение с единицей измерения) | Размер присоединения  
16 |  indexstartaddress | Long | Подустройство ПЛК: Индекс  
17 |  signalrange | Текст | Диапазон сигнала  
18 |  plcbusinterface | Текст | Интерфейс шины: Имя  
19 |  pipeclass | Текст | Класс трубы  
20 |  connectionDesignation | Текст | Обозначения выводов устройства  
21 |  symbol | Текст | Символ (совместимость)  
22 |  idx1 | Текст | Индекс для доп. данных  
23 |  idx2 | Текст | Индекс для доп. данных  
24 |  nesteddevicetag | Текст | Нижестоящее ОУ / идентификатор ОУ  
25 |  safetyrelevant | Булево (истина/ложь) | Защитная функция  
26 |  connectiondescription | Текст | Описания выводов устройства  
27 |  symbolmacro | Текст | Макрос символа (совместимость)  
28 |  connectioncrosssection | Текст (значение с единицей измерения) | Сечение/диаметр вывода  
29 |  combination | Текст | Связка шаблонов (многополюсная)  
30 |  wireconnectionstart | Текст | Начальная часть жилы  
31 |  wireconnectionend | Текст | Концевая часть жилы  
32 |  pos | Короткое целое | Позиция  

Значение некоторых атрибутов зависит от типа изделия:

Группа продуктов |  characteristics |  connectionDesignation* |  idx1 |  idx2 |  terminalNr  
---|---|---|---|---|---  
Общее |  Технические параметры |  Обозначения выводов устройства |  - |  - |  -  
Кабели |  Тип потенциала   
([Список выбора](xmlexport_o_sellists.md#characteristics)) |  Цвет / номер соединения |  Экранировано от |  Парный индекс |  Поперечное сечение / диаметр соединения  
Реле / контакторы |  Технические параметры |  Обозначения выводов устройства |  Индекс контакта / катушки |  - |  -  
Штекеры |  - |  Обозначения выводов устройства |  - |  - |  Обозначение клеммы / контакта штекера  
Клеммы |  - |  Обозначения выводов устройства |  Уровень |  - |  Обозначение клеммы / контакта штекера  
ПЛК |  - |  Обозначения выводов устройства |  Обозначение канала |  - |  Обозначение штекера  

-: Не используется.

*: Разделителем является новая строка.

###  <assemblyposition> <moduleposition>

**№** | **Атрибут** | **Тип** | **Свойство**  
---|---|---|---  
1 |  partnr | Текст | Номер изделия  
2 |  variant | Текст | Вариант  
3 |  count | Long | Количество  
4 |  length | Double | Длина  
5 |  devicetag | Текст | ОУ  
6 |  moduleid | Текст | Идентификатор ОУ  
7 |  posnr | Текст | Номер позиции  
8 |  additionaltext | Текст | Дополнительный текст  
9 |  pos | Короткое целое | Позиция  
10 |  parentvariant | Текст | Вариант узла/модуля  

###  <blockingSurfacePosition>

**№** | **Атрибут** | **Тип** | **Свойство**  
---|---|---|---  
1 |  xpos | Double | Позиция Х  
2 |  ypos | Double | Позиция Y  
3 |  frontside | Булево (истина/ложь) | Передняя сторона  
4 |  width | Double | Ширина  
5 |  height | Double | Высота  
6 |  type | Long | Тип  
7 |  pos | Короткое целое | Позиция  

###  <doorPosition>

**№** | **Атрибут** | **Тип** | **Свойство**  
---|---|---|---  
1 |  xpos | Double | Позиция Х  
2 |  ypos | Double | Позиция Y  
3 |  zpos | Double | Позиция Z  
4 |  partnr | Текст | Дверь: Номер изделия  
5 |  variant | Текст | Дверь: Вариант  
6 |  pos | Короткое целое | Позиция  

###  <mountingPanelPosition>

**№** | **Атрибут** | **Тип** | **Свойство**  
---|---|---|---  
1 |  xpos | Double | Позиция Х  
2 |  ypos | Double | Позиция Y  
3 |  zpos | Double | Позиция Z  
4 |  location | Long (список выбора) | Место установки  
5 |  angle | Double | Углы  
6 |  partnr | Текст | Монтажная плата: Номер изделия  
7 |  variant | Текст | Монтажная плата: Вариант  
8 |  pos | Короткое целое | Позиция  

###  <supportBarPosition>

**№** | **Атрибут** | **Тип** | **Свойство**  
---|---|---|---  
1 |  xpos | Double | Позиция Х  
2 |  ypos | Double | Позиция Y  
3 |  zpos | Double | Позиция Z  
4 |  partnr | Текст | Несущая шина: Номер изделия  
5 |  variant | Текст | Несущая шина: Вариант  
6 |  length | Double | Длина  
7 |  pos | Короткое целое | Позиция  

###  <safetyRelatedValuePosition>

**№** | **Атрибут** | **Тип** | **Свойство**  
---|---|---|---  
1 |  hierarchy1 | Текст (многоязычный) | Параметры, важные с точки зрения безопасности: Уровень иерархии 1  
2 |  hierarchy2 | Текст (многоязычный) | Параметры, важные с точки зрения безопасности: Уровень иерархии 2  
3 |  hierarchy3 | Текст (многоязычный) | Параметры, важные с точки зрения безопасности: Уровень иерархии 3  
4 |  hierarchy4 | Текст (многоязычный) | Параметры, важные с точки зрения безопасности: Уровень иерархии 4  
5 |  hierarchy5 | Текст (многоязычный) | Параметры, важные с точки зрения безопасности: Уровень иерархии 5  
6 |  input | Булево (истина/ложь) | Параметры, важные с точки зрения безопасности: Вход (захват)  
7 |  output | Булево (истина/ложь) | Параметры, важные с точки зрения безопасности: Выход (реакция)  
8 |  logic | Булево (истина/ложь) | Параметры, важные с точки зрения безопасности: Логика (отчет)  
9 |  pl | Текст | Параметры, важные с точки зрения безопасности: PL  
10 |  silcl | Текст | Параметры, важные с точки зрения безопасности: SIL CL  
11 |  pfhd | Double | Параметры, важные с точки зрения безопасности: PFHD  
12 |  tmt1 | Double | Параметры, важные с точки зрения безопасности: TMT1  
13 |  mttfd | Double | Параметры, важные с точки зрения безопасности: MTTFD  
14 |  lambdad | Double | Параметры, важные с точки зрения безопасности: Лямбда-D  
15 |  mttf | Double | Параметры, важные с точки зрения безопасности: MTTF  
16 |  mtbf | Double | Параметры, важные с точки зрения безопасности: MTBF  
17 |  rdf | Double | Параметры, важные с точки зрения безопасности: RDF  
18 |  b10 | Double | Параметры, важные с точки зрения безопасности: B10  
19 |  b10d | Double | Параметры, важные с точки зрения безопасности: B10 D  
20 |  posid | Long | Внутренне: Unique ID  

###  <accessorylist>

**№** | **Атрибут** | **Тип** | **Свойство**  
---|---|---|---  
1 |  P_PART_ACCESSORYLIST_NAME | Текст | Имя (список принадлежностей)  
2 |  P_PART_ACCESSORYLIST_CREATE | Текст | Автор / дата создания (список принадлежностей)  
3 |  P_PART_ACCESSORYLIST_DESCRIPTION | Текст (многоязычный) | Описание (список принадлежностей)  
4 |  P_PART_ACCESSORYLIST_LASTCHANGE | Текст | Последний обработчик / дата изменения (список принадлежностей)  
5 |  P_PART_LASTCHANGE_USER | Текст | Последний обработчик  
6 |  P_PART_CREATE_USER | Текст | Автор  
7 |  P_PART_CREATE_DATE_UTC | Целое число (время) | Дата создания (UTC)  
8 |  P_PART_LASTCHANGE_DATE_UTC | Целое число (время) | Дата изменения (UTC)  
9 |  P_ARTICLEACCESSORYLIST_INSERT_COMPLETE | Булево (истина/ложь) | Вставить полностью список принадлежностей  

###  <accessorylistposition>

**№** | **Атрибут** | **Тип** | **Свойство**  
---|---|---|---  
1 |  placement | Текст | Размещение принадлежностей  
2 |  partnr | Текст | Номер изделия  
3 |  variant | Текст | Вариант  
4 |  pos | Короткое целое | Позиция  

###  <accessoryplacement>

**№** | **Атрибут** | **Тип** | **Свойство**  
---|---|---|---  
1 |  P_PART_ACCESSORYPLACEMENT_NAME | Текст | Имя (размещение принадлежностей)  
2 |  P_PART_ACCESSORYPLACEMENT_CREATE | Текст | Автор / дата создания (размещение принадлежностей)  
3 |  P_PART_ACCESSORYPLACEMENT_DESCRIPTION | Текст (многоязычный) | Описание (размещение принадлежностей)  
4 |  P_PART_ACCESSORYPLACEMENT_LASTCHANGE | Текст | Последний обработчик / дата изменения (размещение принадлежностей)  
5 |  P_PART_LASTCHANGE_USER | Текст | Последний обработчик  
6 |  P_PART_CREATE_USER | Текст | Автор  
7 |  P_PART_CREATE_DATE_UTC | Целое число (время) | Дата создания (UTC)  
8 |  P_PART_LASTCHANGE_DATE_UTC | Целое число (время) | Дата изменения (UTC)  

###  <accessoryplacementposition>

**№** | **Атрибут** | **Тип** | **Свойство**  
---|---|---|---  
1 |  name | Текст | Варианты установки  
2 |  referencepoint | Long | Исходная точка  
3 |  rotation | Double | Поворот  
4 |  xspacing | Double | Смещение в направлении X  
5 |  yspacing | Double | Смещение в направлении Y  
6 |  zspacing | Double | Смещение в направлении Z  
7 |  movable | Булево (истина/ложь) | Перемещаемый  
8 |  pos | Короткое целое | Позиция  

###  <construction>

**№** | **Атрибут** | **Тип** | **Свойство**  
---|---|---|---  
1 |  P_PART_CONSTRUCTION_NAME | Текст | Имя  
2 |  P_PART_CONSTRUCTION_CREATE | Текст | Автор / дата создания (схема сверления)  
3 |  P_PART_CONSTRUCTION_DESCRIPTION | Текст (многоязычный) | Описание (схема сверления)  
4 |  P_PART_CONSTRUCTION_LASTCHANGE | Текст | Последний обработчик / дата изменения (схема сверления)  
5 |  P_PART_CONSTRUCTION_VARIANT | Текст | Вариант схемы сверления  
6 |  P_PART_LASTCHANGE_USER | Текст | Последний обработчик  
7 |  P_PART_CREATE_USER | Текст | Автор  
8 |  P_PART_CREATE_DATE_UTC | Целое число (время) | Дата создания (UTC)  
9 |  P_PART_LASTCHANGE_DATE_UTC | Целое число (время) | Дата изменения (UTC)  

###  <drillingPosition>

**№** | **Атрибут** | **Тип** | **Свойство**  
---|---|---|---  
1 |  type | Long (список выбора) | Тип сверления  
2 |  subtype | Long (список выбора) | Подтип  
3 |  outlinename | Текст | Название контура  
4 |  xpos | Double | Позиция Х  
5 |  ypos | Double | Позиция Y  
6 |  angle | Double | Углы  
7 |  dimension1 | Double | 1-е измерение  
8 |  dimension2 | Double | 2-е измерение  
9 |  dimension3 | Double | 3-е измерение  
10 |  spacingrepeat | Double | Интервал повтора  
11 |  spacingend | Double | Конечный интервал  
12 |  drillnthhole | Long | Просверл. кажд. n-е отверст.  
13 |  fabricatealways | Булево (истина/ложь) | Всегда создавать  
14 |  pos | Long | Внутренне: Position (drilling pattern)  

###  <terminal>

**№** | **Атрибут** | **Тип** | **Свойство**  
---|---|---|---  
1 |  P_PART_TERMINAL_NAME | Текст | Имя (схема соединений)  
2 |  P_PART_TERMINAL_ADDITIONALLENGTHDEFAULT | Double | Дополнительная длина (стандарт)  
3 |  P_PART_TERMINAL_CREATE | Текст | Автор / дата создания (схема соединений)  
4 |  P_PART_TERMINAL_DESCRIPTION | Текст (многоязычный) | Описание (схема соединений)  
5 |  P_PART_TERMINAL_DIRECTION | Long (список выбора) | Направление подсоединения (стандарт)  
6 |  P_PART_TERMINAL_LASTCHANGE | Текст | Последний обработчик / дата изменения (схема соединений)  
7 |  P_PART_TERMINAL_TERMINALSIZE_DEFAULT | Текст (значение с единицей измерения) | Размер присоединения (стандарт)  
8 |  P_PART_TERMINAL_TYPEDEFAULT | Long | Обработка концов проводов (Eplan Cabinet, станд.)  
9 |  P_PART_TERMINAL_TYPEOFTERMINAL_DEFAULT | Long (список выбора) | Категория соединения (стандарт)  
10 |  P_PART_LASTCHANGE_USER | Текст | Последний обработчик  
11 |  P_PART_CREATE_USER | Текст | Автор  
12 |  P_PART_CREATE_DATE_UTC | Целое число (время) | Дата создания (UTC)  
13 |  P_PART_LASTCHANGE_DATE_UTC | Целое число (время) | Дата изменения (UTC)  

###  <terminalPosition>

**№** | **Атрибут** | **Тип** | **Свойство**  
---|---|---|---  
1 |  name | Текст | Обозначение вывода устройства  
2 |  xpos | Двойное значение (координата) | Позиция Х  
3 |  ypos | Двойное значение (координата) | Позиция Y  
4 |  zpos | Двойное значение (координата) | Позиция Z  
5 |  direction | Long | Направление подсоединения  
6 |  additionallength | Двойное значение (координата) | Доп. длина  
7 |  type | Long | Обработка концов проводов (Eplan Cabinet)  
8 |  mincrosssection | Двойное значение (координата) | Мин. поперечное сечение  
9 |  maxcrosssection | Двойное значение (координата) | Макс. поперечное сечение  
10 |  maxwirecount | Long | Макс. число соединений  
11 |  twinsleeve | Булево (истина/ложь) | Предписать двойную трубку  
12 |  typeofterminal | Long | Категория соединения  
13 |  terminalsize | Текст (значение с единицей измерения) | Размер присоединения  
14 |  devicetag | Текст | Обозначение штекера  
15 |  level | Long | Уровень  
16 |  targetinfo | Long | Внутр./внешн. индекс  
17 |  xdir | Двойное значение (координата) | Вектор X  
18 |  ydir | Двойное значение (координата) | Вектор Y  
19 |  zdir | Двойное значение (координата) | Вектор Z  
20 |  pos | Long | Внутренне: Position (connection point pattern)  
21 |  mincrosssectionawg | Текст | Мин. AWG  
22 |  maxcrosssectionawg | Текст | Макс. AWG  
23 |  screwdrives | Текст | Размер наконечника  
24 |  plcbusinterface | Текст | Интерфейс шины: Имя  
25 |  mintorque | Double | Мин. момент затяжки  
26 |  maxtorque | Double | Макс. момент затяжки  
27 |  strippinglength | Double | Длина зачистки  
28 |  opvecxpos | Двойное значение (координата) | Положение инструмента по оси X  
29 |  opvecypos | Двойное значение (координата) | Положение инструмента по оси Y  
30 |  opveczpos | Двойное значение (координата) | Положение инструмента по оси Z  
31 |  opvecxdir | Двойное значение (координата) | Вектор инструмента по оси X  
32 |  opvecydir | Двойное значение (координата) | Вектор инструмента по оси Y  
33 |  opveczdir | Двойное значение (координата) | Вектор инструмента по оси Z  
34 |  holediameter | Double | Диаметр вала  
35 |  clampspaceoffset | Double | Выступ полости вывода  
36 |  clampspacexstart | Двойное значение (координата) | Начальная точка полости обжима по оси X  
37 |  clampspaceystart | Двойное значение (координата) | Начальная точка полости обжима по оси Y  
38 |  clampspacezstart | Двойное значение (координата) | Начальная точка полости обжима по оси Z  
39 |  clampspacexend | Двойное значение (координата) | Конечная точка полости обжима по оси X  
40 |  clampspaceyend | Двойное значение (координата) | Конечная точка полости обжима по оси Y  
41 |  clampspacezend | Двойное значение (координата) | Конечная точка полости обжима по оси Z  

###  <address>

**№** | **Атрибут** | **Тип** | **Свойство**  
---|---|---|---  
1 |  class | Long | Тип записи данных  
2 |  P_PART_ADDRESS_SHORTNAME | Текст | Краткое имя  
3 |  P_PART_ADDRESS_EMAIL | Текст | Электронная почта  
4 |  P_PART_ADDRESS_FAX | Текст | Факс  
5 |  P_PART_ADDRESS_LASTCHANGE | Текст | Последний обработчик / дата изменения (адрес)  
6 |  P_PART_ADDRESS_LONGNAME | Текст | Полное имя  
7 |  P_PART_ADDRESS_NAME1 | Текст | Имя 1  
8 |  P_PART_ADDRESS_NAME2 | Текст | Имя 2  
9 |  P_PART_ADDRESS_NAME3 | Текст | Имя 3  
10 |  P_PART_ADDRESS_NOTE | Текст (многоязычный) | Описание (адрес)  
11 |  P_PART_ADDRESS_NUMBER | Текст | Номер клиента  
12 |  P_PART_ADDRESS_PHONE | Текст | Телефон  
13 |  P_PART_ADDRESS_POBOX | Текст | Почт. ящик  
14 |  P_PART_ADDRESS_STATE | Текст | Страна  
15 |  P_PART_ADDRESS_STREET | Текст | Улица  
16 |  P_PART_ADDRESS_TITLE | Текст | Обращение  
17 |  P_PART_ADDRESS_TOWN | Текст | Место жительства  
18 |  P_PART_ADDRESS_ZIPPOBOX | Текст | Почт. индекс (почт. ящик)  
19 |  P_PART_ADDRESS_ZIPTOWN | Текст | Почтовый индекс (место жительства)  
20 |  P_PART_LASTCHANGE_USER | Текст | Последний обработчик  
21 |  P_PART_CREATE_DATE_UTC | Целое число (время) | Дата создания (UTC)  
22 |  P_PART_LASTCHANGE_DATE_UTC | Целое число (время) | Дата изменения (UTC)  

###  <propertydefinition>

**№** | **Атрибут** | **Тип** | **Свойство**  
---|---|---|---  
1 |  identname | Текст | Идентифицирующее имя  
2 |  category | Long | Категория  
3 |  datatype | Long | Тип данных  
4 |  sigroup | Long | Группа единиц измерения  
5 |  siunit | Long | Единица измерения  
6 |  P_DMUSERPROPDEFTABLEENTRY_DESCRIPTION | Текст (многоязычный) | Описание  
7 |  P_DMUSERPROPDEFTABLEENTRY_DISPLAYNAME | Текст (многоязычный) | Отображаемое имя  
8 |  propuser | Тексты (разделенные табуляцией) | Присвоения  
9 |  proptype | Long | Помощь ввода  
10 |  P_DMUSERPROPDEFTABLEENTRY_INPUTASSISTANCE_VALUE | Тексты (многоязычные, разделенные табуляцией) | Значение по умолчанию для списка выбора  
11 |  unused | Булево (истина/ложь) | Больше не использовать  
12 |  translateflag | Булево (истина/ложь) | Перевести значение свойства  

### Группы единиц измерения

#### Основная единица измерения

**Внутреннее значение** | ****  
---|---  
0 | Основная единица измерения  

#### Длина

**Внутреннее значение** | **Отображаемое значение** | **Основная единица измерения**  
---|---|---  
256 | мкм |   
258 | мкм |   
259 | мм |   
261 | мм |   
262 | см |   
264 | см |   
265 | дм |   
267 | дм |   
268 | м | x  
269 | Meter |   
271 | м |   
272 | км |   
274 | км |   
295 | mile |   
294 | мил |   
275 | In |   
276 | дюйм |   
277 | дюйм |   
293 | Дюйм |   
278 | " |   
279 | фут |   
280 | футов |   
281 | фут |   
282 | ярд |   
283 | ярд |   
284 | # |   
285 | Настройка пользователя: Единица отображения длины |   
286 | Настройка проекта: соединения / кабели |   
287 | Настройка проекта: соединения / электротехника |   
288 | Настройка проекта: соединения / гидравлика |   
289 | Настройка проекта: соединения / пневматика |   
290 | Настройка проекта: соединения / охлаждение |   
291 | Настройка проекта: соединения / смазка |   
292 | Настройка проекта: соединения / технология производственных процессов |   

#### Масса

**Внутреннее значение** | **Отображаемое значение** | **Основная единица измерения**  
---|---|---  
512 | µg |   
514 | мкг |   
515 | mg |   
517 | мг |   
518 | г |   
520 | г |   
521 | Pfund |   
522 | кг | x  
524 | кг |   
525 | Ztr |   
526 | dz |   
527 | t |   
529 | т |   
530 | oz |   
531 | фунт |   
532 | lbs |   
533 | Karat |   
534 | Настройка пользователя: отображение единицы веса |   
535 | tn.sh |   

#### Время

**Внутреннее значение** | **Отображаемое значение** | **Основная единица измерения**  
---|---|---  
768 | µs |   
770 | мкс |   
771 | ms |   
773 | мс |   
774 | s | x  
776 | с |   
777 | min |   
779 | мин |   
780 | ч |   
782 | ч |   
783 | d |   
785 | дн |   

#### Частота

**Внутреннее значение** | **Отображаемое значение** | **Основная единица измерения**  
---|---|---  
1024 | Гц | x  
1025 | kHz |   
1026 | MHz |   
1027 | GHz |   

#### Сила электрического тока

**Внутреннее значение** | **Отображаемое значение** | **Основная единица измерения**  
---|---|---  
1280 | µA |   
1282 | мкА |   
1283 | mA |   
1285 | мА |   
1286 | A | x  
1288 | А |   
1289 | kA |   
1291 | кА |   
1292 | MA |   
1294 | МА |   

#### Электрическое напряжение

**Внутреннее значение** | **Отображаемое значение** | **Основная единица измерения**  
---|---|---  
1536 | µV |   
1538 | мкВ |   
1539 | mV |   
1541 | мВ |   
1542 | V | x  
1544 | В |   
1545 | kV |   
1547 | кВ |   
1548 | MV |   
1550 | МВ |   

#### Электрическое сопротивление

**Внутреннее значение** | **Отображаемое значение** | **Основная единица измерения**  
---|---|---  
1792 | µΩ |   
1793 | mΩ |   
1794 | Ω | x  
1795 | kΩ |   
1796 | MΩ |   
1797 | GΩ |   
1798 | S |   

#### Мощность

**Внутреннее значение** | **Отображаемое значение** | **Основная единица измерения**  
---|---|---  
2048 | µW |   
2049 | mW |   
2050 | W | x  
2051 | kW |   
2052 | MW |   
2053 | GW |   
2054 | hp |   
2055 | PS |   
2056 | kJ/h |   
2057 | kJ/min |   
2058 | kJ/s |   
2059 | BTU/h |   
2060 | BTU/min |   
2061 | BTU/s |   
2062 | V*A |   

#### Температура

**Внутреннее значение** | **Отображаемое значение** | **Основная единица измерения**  
---|---|---  
2304 | K | x  
2305 | °C |   
2306 | °Ra |   
2307 | °Re |   
2308 | °F |   

#### Давление

**Внутреннее значение** | **Отображаемое значение** | **Основная единица измерения**  
---|---|---  
2560 | µPa |   
2561 | mPa |   
2562 | Па | x  
2563 | hPa |   
2564 | kPa |   
2570 | МПа |   
2565 | mbar |   
2566 | мбар |   
2567 | бар |   
2568 | Torr |   
2569 | psi |   

#### Работа

**Внутреннее значение** | **Отображаемое значение** | **Основная единица измерения**  
---|---|---  
2816 | µJ |   
2817 | mJ |   
2818 | Дж | x  
2819 | kJ |   
2820 | MJ |   
2821 | GJ |   
2822 | Cal |   
2823 | Н∙м |   
2824 | Ws |   
2825 | kWs |   
2826 | Wh |   
2827 | kWmin |   
2828 | kWh |   

#### Количество вещества

**Внутреннее значение** | **Отображаемое значение** | **Основная единица измерения**  
---|---|---  
3072 | µmol |   
3073 | mmol |   
3074 | моль | x  
3075 | kmol |   
3076 | Mmol |   

#### Сила света

**Внутреннее значение** | **Отображаемое значение** | **Основная единица измерения**  
---|---|---  
3328 | µcd |   
3329 | mcd |   
3330 | кд | x  
3331 | kcd |   
3332 | Mcd |   

#### Площадь

**Внутреннее значение** | **Отображаемое значение** | **Основная единица измерения**  
---|---|---  
3604 | мкм² |   
3594 | qmm |   
3584 | мм² |   
3585 | cm² |   
3586 | dm² |   
3587 | м² | x  
3588 | a |   
3589 | ha |   
3590 | km² |   
3591 | дюйм² |   
3592 | ft² |   
3593 | yd² |   
3597 | cmil |   
3596 | kcmil |   
3595 | MCM |   
3598 | мм² |   
3599 | см² |   
3600 | дм² |   
3601 | м² |   
3602 | км² |   
3603 | mile² |   

#### Объем

**Внутреннее значение** | **Отображаемое значение** | **Основная единица измерения**  
---|---|---  
3840 | ml |   
3841 | л | x  
3843 | л |   
3844 | hl |   
3845 | m³ |   
3847 | м³ |   
3848 | qm |   
3849 | mm³ |   
3850 | cm³ |   
3851 | cl |   
3852 | dl |   
3853 | dm³ |   
3854 | in³ |   
3855 | ft³ |   
3856 | yd³ |   
3857 | fl.oz |   
3858 | pt |   
3859 | gal |   

#### Угол

**Внутреннее значение** | **Отображаемое значение** | **Основная единица измерения**  
---|---|---  
4096 | ° | x  
4097 | рад |   

#### Масса на длину

**Внутреннее значение** | **Отображаемое значение** | **Основная единица измерения**  
---|---|---  
4352 | g/km |   
4353 | г/м | x  
4354 | g/mm |   
4355 | kg/m |   
4362 | kg/km |   
4356 | lb/in |   
4357 | lb/ft |   
4358 | lb/yd |   
4359 | oz/in |   
4360 | oz/ft |   
4361 | oz/yd |   

#### Объемный поток

**Внутреннее значение** | **Отображаемое значение** | **Основная единица измерения**  
---|---|---  
4608 | л/ч |   
4609 | л/мин |   
4610 | л/с | x  
4611 | mm³/h |   
4612 | mm³/min |   
4613 | mm³/s |   
4614 | ml/h |   
4615 | ml/min |   
4616 | ml/s |   
4617 | cm³/h |   
4618 | cm³/min |   
4619 | cm³/s |   
4620 | cl/h |   
4621 | cl/min |   
4622 | cl/s |   
4623 | dl/h |   
4624 | dl/min |   
4625 | dl/s |   
4626 | dm³/h |   
4627 | dm³/min |   
4628 | dm³/s |   
4629 | hl/h |   
4630 | hl/min |   
4631 | hl/s |   
4632 | m³/h |   
4633 | m³/min |   
4634 | m³/s |   
4635 | in³/h |   
4636 | in³/min |   
4637 | in³/s |   
4638 | ft³/h |   
4639 | ft³/min |   
4640 | ft³/s |   
4641 | yd³/h |   
4642 | yd³/min |   
4643 | yd³/s |   
4644 | fl.oz/h |   
4645 | fl.oz/min |   
4646 | fl.oz/s |   
4647 | pt/h |   
4648 | pt/min |   
4649 | pt/s |   
4650 | gal/h |   
4651 | gal/min |   
4652 | gal/s |   

#### Массовый поток

**Внутреннее значение** | **Отображаемое значение** | **Основная единица измерения**  
---|---|---  
4864 | kg/h |   
4865 | kg/min |   
4866 | кг/с | x  
4867 | t/h |   
4868 | t/min |   
4869 | t/s |   
4870 | tn.sh/h |   
4871 | tn.sh/min |   
4872 | tn.sh/s |   
4873 | lb/h |   
4874 | lb/min |   
4875 | lb/s |   
4876 | oz/h |   
4877 | oz/min |   
4878 | oz/s |   
4879 | g/min |   

#### Размер файла

**Внутреннее значение** | **Отображаемое значение** | **Основная единица измерения**  
---|---|---  
5120 | байт | x  
5121 | КБ |   
5122 | МБ |   
5123 | ГБ |   
5124 | TB |   

#### Скорость передачи данных

**Внутреннее значение** | **Отображаемое значение** | **Основная единица измерения**  
---|---|---  
5376 | bps | x  
5377 | Kbps |   
5378 | Mbps |   
5379 | Gbps |   
5380 | Tbps |   

#### Число

**Внутреннее значение** | **Отображаемое значение** | **Основная единица измерения**  
---|---|---  
5632 | Stück | x  
5633 | stk. |   
5634 | pc. |   
5635 | шт. |   

#### Электрическая проводимость

**Внутреннее значение** | **Отображаемое значение** | **Основная единица измерения**  
---|---|---  
5891 | MS/m |   
5888 | S/m | x  
5889 | S/cm |   
5890 | S/in |   

#### Температурный коэффициент

**Внутреннее значение** | **Отображаемое значение** | **Основная единица измерения**  
---|---|---  
6144 | 1/K | x  

#### Частота вращения

**Внутреннее значение** | **Отображаемое значение** | **Основная единица измерения**  
---|---|---  
6400 | U/min | x  
6401 | U/sek |   
6402 | rpm |   
6403 | rps |   
6404 | /min |   
6405 | /s |   
6406 | /h |   

#### Масса на объем

**Внутреннее значение** | **Отображаемое значение** | **Основная единица измерения**  
---|---|---  
6656 | kg/m³ | x  
6657 | g/m³ |   
6658 | mg/m³ |   

#### Скорость

**Внутреннее значение** | **Отображаемое значение** | **Основная единица измерения**  
---|---|---  
6912 | m/s | x  
6913 | km/h |   
6914 | mph |   
6915 | kn |   
6916 | ft/s |   

#### Динамическая вязкость

**Внутреннее значение** | **Отображаемое значение** | **Основная единица измерения**  
---|---|---  
7168 | Pa*s | x  
7169 | kg/m*s |   

#### Электрическая емкость

**Внутреннее значение** | **Отображаемое значение** | **Основная единица измерения**  
---|---|---  
7424 | F | x  
7425 | mF |   
7426 | µF |   
7427 | nF |   

#### Звуковое давление

**Внутреннее значение** | **Отображаемое значение** | **Основная единица измерения**  
---|---|---  
7680 | dB | x  
7681 | dB(A) |   

#### Выброс

**Внутреннее значение** | **Отображаемое значение** | **Основная единица измерения**  
---|---|---  
7936 | g/kWh | x  
7937 | kg/kWh |   
7938 | mg/kWh |   
7939 | kg/TJ |   

#### Момент инерции

**Внутреннее значение** | **Отображаемое значение** | **Основная единица измерения**  
---|---|---  
8192 | kg*m² | x  

#### Теплопроводность

**Внутреннее значение** | **Отображаемое значение** | **Основная единица измерения**  
---|---|---  
8448 | W/K | x  

#### Процент

**Внутреннее значение** | **Отображаемое значение** | **Основная единица измерения**  
---|---|---  
8704 | % | x  

#### Стандартный объемный расход

**Внутреннее значение** | **Отображаемое значение** | **Основная единица измерения**  
---|---|---  
8960 | ln/s | x  
8961 | ln/min |   
8962 | mln/min |   

#### Относительная влажность воздуха

**Внутреннее значение** | **Отображаемое значение** | **Основная единица измерения**  
---|---|---  
9216 | %RH | x
