###Лабораторна робота 1
#Розробка програми керування доступом до захищеного носія інформації 
Програма після завантаження в оперативну пам'ять здійснює контроль за спробами доступу до диску шляхом перехоплення відповідних переривань (21Н та ін). У результаті управління передається програмам парольного захисту, і в залежності від статусу “admin” чи “user”, після реєстрації вони отримують відповідні дискретні права доступу до логічних дисків А, В, С та / або права читання, запису і / або виконання (за варіантами) до файлів на дисках.