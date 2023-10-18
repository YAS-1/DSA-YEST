

catholic_martyrs = ['Achileo Kiwanuka','Adolphus Ludigo','Mukasa','Ambrosius','Kibuuka','Anatoli','Kiriggwajjo','Andrew Kaggwa','Antanasio','Bazzekuketta','Bruno','Sserunkuma','Charles Lwanga','Denis','Ssebuggwawo','Wasswa','Gonzaga Gonza','Gyavira Musoke','Yowana Mukiibi','Yusufu Lugalama','Zakayo Lubega','James','Buuzaabalyawo','Muzeeyi','John Maria','Joseph Mukasa','Kizito','Lukka','Baanabakintu','Matiya Mulumba','Mbaga Tuzinde','Mugagga Lubowa','Mukasa','Kiriwawanvu','Nowa Mawaggali','Ponsiano','Ngondwe']

Anglican_martyrs = ['Aaron Lubega','Apollo Kivebulaya','Eria Sebukyala','Fredrick Kizza','George Kizza','James Hannington','Janani Luwum','Joseph','Balikuddembe','Kizito','Mark Kkumba','Matia Mulumba','Nuhu Mbegu','Robert','Munyagayirwa','Samwiri Mukasa','Yefusa Namayanja','Yohana Mukasa','Yosefu Lugalama','Yowana Kitaka','Yowana Maria','Mukasa']

catholic_martyrs = list(set(catholic_martyrs))
Anglican_martyrs = list(set(Anglican_martyrs))

martyr_count = input('Enter a name of a martyr: ')
if martyr_count in catholic_martyrs:
    print('He was Catholic Martyr')
elif martyr_count in Anglican_martyrs:
    print('He was an Anglican Martyr')
e