#!/bin/bash
 num=1
produto=("3m
Aeolus
Afp
Ahead Sports
Air Hawk
Airfix
Airhawk
Airpump
Ajax
Alba Eletrônicos
Alliance
Altura
Alvamine
American Pets
Annaite
Antares
Aplus
Apollo
Aptany
Arisun
Armom
Armour
Artliber
Artmed
Artum
Askein
Astro
Atheneu
Atrezzo
Atrio
Atturo
Aushine
Barile
Barum
Baston
Baxmann
Bct
Belfix
Belshina
Bepo
Bering
Bestway
Beto
Beyond
Bfgoodrich
Biker
Black Bull
Black Jack
Blacklion
Blu Editora
Bolex
Bonna
Bontrager
Borilli Racing
Boristar
Bosch
Boto
Bovenau
Bozza
Braclean
Bracol
Brandy
Brasfort
Brasplus
Bremen
Bridgestone
Briland
Buffalo
Butterworth-heinemann
Cadillac
Camper
Carrera
Ceat
Centralsul
Champiro
Chao Yang
Cheng Shin Tire
Chengshan
Chiaperini
Chimpa
Cinborg
Classic
Clear
Cm
Comforser
Condor
Constancy
Continental
Cooper
Cordiant
Covertech
Cr
Cressi Sub
Cst
Daewoo
Dayton
Deestone
Deli Tires
Delinte
Delium
Dewalt
Dhk
Digimess
Dinodog
Disma
Divicar
Domani
Dpl
Drc
Dropboards
Drywash
Dsi
Dsr
Dueler
Dunlop
Dunlop /
Durun
Durun Tires
Eastgomma
Eccofer
Echolife
Ecovision /
Eda
Eda/excellent
Effetto Mariposa
Elastobor
Erica
Euro
Euzkadi
Falken
Fate
Firestone
Flash Cover
Flexen
Flush
Foca Louca
Ford
Forerunner
Forever
Front Rubber
Full Bore
Fullway
Fun Motors
Fundacentro
Fuzion
Gallant
Garmin
Gauss
Geax
General
Genius
Gianelli
Gison
Giti
Givi
Giyo
Goform
Goodride
Goodyear
Grand Car
Greatair
Green-max
Greenbelt
Gripmax
Gt
Champiro
Maxmiler
Radial
Gtsm1
Habilead
Haida
Hankook
Headway
Heidenau
Hemus
Hero
Hifly
Honour
Horizon
Horizon /
Hot Wheels
Houston
Hymair
Ibex Publishers Pod
Ilink
Ims
Intex
Ira
Irc
Jambo
Jatp-mg
Jinshuai
Jinyu
Jk
Jkt Rs
Joes
Joyroad
Kajima
Kb50
Kelly
Kenda
Kinesio Tape
King Tony
Kits
Kmach
Kombat
Kumho
Kyoto
Lande
Landsail
Laufenn
Laufenn By Hankook
Lcm Bolas
Ldr2
Levorin
Leão Tire
Lider
Ling Long
Link
Long March
Lotus
Ltc
Ltc Didático
Lucabor
Luzian
Macaulay
Maggion
Malhotra
Marcher
Marcon
Marshal
Mastercraft
Mastersteel
Mavic
Maxine
Maxisport
Maxtrek
Maxxis
Mazzini
Mc
Medlevensohn
Meganovidades
Meguiars
Metalcava
Metalosa
Metezeler
Metzeler
Michelin
Mitas
Momo
Mor
Mothers
Motul
Mr Maquinas Riberiro
Mr Pet
Mrf
Mtx
Mwm
Nama
Nankang
Nautika
Nexen
Oasis
Odyking
Oko
Onyx
Orbi Quimica
Ornet
Ortometal
Ortopedia Jaguaribe
Otani
Otr Max
Ovation
Pacar
Pace
Passage
Pearl River
Peccinin
Pegasus
Performance
Permanent
Perola
Pet Flex
Petlas
Petlike
Pioner
Pirell
Pirelli
Piu Blu
Plana
Planatc
Plug Kit
Porter Cable
Power Trac
Premiorri
Premium
Pressure
Prestovac
Primewell
Proauto
Propek
Protector
Pérola
Radar
Ranger
Raven
Regal
Represent
Ressolado
Rhino King
Rhoden
Rinaldi
Rintal
Roadstone
Roca
Rosava /
Rotalla
Rua
Rubena
Runking
Runway
Ruzi
Rydanz
Sagyma
Sailun
Samson 
Santyre 
Schrader
Schulz
Schwalbe
Schweers
Seasub
Seiberling
Semperit
Shutt
Sigma
Sk
Skil
Slime
Soft99
Sonar
Sonax
Songe
Soniclear
Sonnar
Sonny
Soteco
Spumbril
Stampjet
Stanley
Star Performer
Starfer
Starfire
Start Racing
Steula
Sttones
Sun Car
Sun-f
Sunitrac
Sunny
Suntek
Taifa
Taishan
Tecfil
Tewak
Thompson
Three-a
Thule
Thunderer
Thz
Tigar
Tigar Hitris
Timberline
Tito Bikes
Topeak
Toyo
Treadura
Trelleborg
Tri-ace
Triangle
Tufo
Turtle Wax
Two Dogs
Tyfoon
Ultra Airfix
Ultratyre
Unifort
Uniglory
Unigrip
Unipro Editora
Us Boards
Vee Rubber
Vellux
Verden
Vipal
Vittoria
Vonder
Vonixx
Vozes
Vto
Vzan
Waft
Wanda King
Wanli
Weldtite
Western
Westlake
Winrun
Worker
Wtb
Xbri
Xplore
Xpoynt
Xtire
Yaay
Yamar
Yellow
Yellowsea
Yokohama
Zaffiro Pro
Zefal
Zeta
Zetta
Zetum
Zimedical
ática
")
touch /home/nicholas/workspace.odysci_ecommerce/e-commerce-admin/conf/groups-pro/lists/marca/pneu.txt
echo "	">/home/nicholas/workspace.odysci_ecommerce/e-commerce-admin/conf/groups-pro/lists/marca/pneu.txt
for produtos in $produto
 do
 	
	echo "	"[[$produtos]]>> /home/nicholas/workspace.odysci_ecommerce/e-commerce-admin/conf/groups-pro/lists/marca/pneu.txt
	echo "	""	"$produtos>> /home/nicholas/workspace.odysci_ecommerce/e-commerce-admin/conf/groups-pro/lists/marca/pneu.txt
	
done

