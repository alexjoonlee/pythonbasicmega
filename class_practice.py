# albums = []
# def singer(name, album):
#     albums.append(album)
#     return albums

class album_of_singer():
    # 속성, 변수수
    def __init__(self, name):
        self.name = name
        self.albums = []
    # 기능
    def add_album(self, album):
        self.albums.append(album)
        return self.albums
    
bts = album_of_singer('BTS')
bts.add_album('1집')
bts.add_album('2집')
bts.add_album('3집')
print('BTS:', bts.albums)

bp = album_of_singer('BP')
bp.add_album('1집')
bp.add_album('2집')
print("BP:", bp.albums)

# bts = singer('BTS','1집')
# print(bts)

# bts = singer('BTS','2집')
# print(bts)

# bts = singer('BTS','3집')
# print(bts)

# bpink = singer('BP', '집')
# print(bpink)