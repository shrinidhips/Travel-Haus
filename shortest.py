def short(mat,district,place):
    ans=mat[district.index(place)].index(min(mat[district.index(place)]))
    print(district[ans])
vijayanagara=[
    'TB dam',
    'Virupaksha temple', 
    'Saasivekeelu Ganesha',
    'lotus mahal', 
    'Tenali Rama pavilion', 
    'Octagonal bath', 
    'Stone chariot']
vijayanagara_distance_matrix=[
	[1000,19,18,18,18,18,23],
	[19,1000,1,4,3,4,10],
	[18,1,1000,3,3,4,9],
	[18,4,3,1000,1,2,7],
	[18,3,3,1,1000,2,7],
	[18,4,4,2,2,1000,6],
	[23,10,9,7,7,6,1000]]
coorg= [
'Dubarey elephant camp' , 
'Talakaveri' ,
'Malalli falls' ,
'Kumaraparvatha' ,
'Mandalpatti' ,
'Tadiundamol' ,
'Abbey falls' ]

coorg_distance_matrix = [ [1000,70,56,61,46,63,40],
[70,1000,96,101,57,42,49],
[56,96,1000,9,70,94,56],
[61,101,9,1000,67,98,61],
[46,55,62,67,1000,52,10],
[63,42,94,98,54,1000,46],
[40,49,56,61,10,46,1000] ]

chikmagalur= ['Rani Jhari' , 'Kudremukh' ,'EthinaBhuja' , 'Devaramane' , 'Baba budangiri'  , 'Kemmangundi' , 'Khythanamakki']

chikmagalur_distance_matrix=[ [1000,48,59,47,103,126,46],
[48,1000,94,85,139,168,37],
[59,94,1000,22,89,104,91],
[47,85,22,1000,84,113,79],
[103,139,89,84,1000,79,107],
[116,168,104113,79,1000,153],
[46,37,91,79,107,153,1000] ]

manglore=[
'Kudroli Temple',
'New mangalore port ',
'Mangaladevi temple ',
'Panambur beach ',
'Ullal beach ',
'Surathkal Beach',
'Pilikula Nisargadhama'
]
manglore_distance_matrix =[ [1000,9,4,10,13,16,13],
[9,1000,15,3,19,9,11],
[4,15,1000,15,8,21,16],
[10,3,15,1000,21,8,13],
[13,19,8,21,1000,26,20],
[16,9,21,8,26,1000,19],
[13,11,16,13,20,19,1000] ]

mysore=[
'mysore palace',
'chamundi hill',
'St Philomena’s Cathedral',
'mysore sand sculpture museum',
'talakad',
'Sri Chamarajendra Zoological Gardens',
'Brindavan Gardens'
]
mysore_distance_matrix =[ [1000,12,2,5,48,2,20],
[12,1000,13,8,52,10,31],
[2,13,1000,5,48,5,20],
[5,8,5,1000,51,4,17],
[48,52,48,51,1000,46,67],
[2,10,5,4,46,1000,21],
[20,31,20,17,67,21,1000] ]

short(mysore_distance_matrix,mysore,'chamundi hill')