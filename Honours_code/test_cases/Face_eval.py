import http.client, urllib, base64
from pprint import pprint 
import json
import sys 
from azure.cognitiveservices.search.imagesearch import ImageSearchAPI
from msrest.authentication import CognitiveServicesCredentials  
from PIL import Image 
import urllib.request  
import urllib.error
import os  
import random
from cognitive_face import face
from azure.cognitiveservices.search.imagesearch.models.image_search_api_enums import ImageContent
from numpy.lib.function_base import average




vpeople = '''-Howard Aiken -Frances E Allen -John Atanasoff -Charles Babbage-John Backus-Corrado bohm-Fred Brooks-Vannevar Bush-Vint Cerf-Noam Chomsky-Edmund Clarke-Lynn Conway -Stephen Cook-Edsger Dijkstra -Ermest Allen Emerson -Douglas Engelbart-Federico Faggin-Elizabeth Feinler-Tommy Flowers-Sally Floyd-Charles Sanders Pierce-Stephen Furber-Sophie Wilson-Seymour Ginsburg-Susan L graham-Jim Gray-Barbara Grosz-Margaret Hamilton-Geoffrey Hinton-Charles Anthony Richard Hoare -Betty Holberton-Harry Huskey-Kenneth Iverson-Karen Sparck Jones-Jacek Karpinski -Alan Kay-Stephen Cole Kleene-Donald Knuth-Leslie Lamport-Barbara Liskov-Ada Lovelace-John McCarthy-Marvin Minsky-Yoshiro Nakamatsu-Akira Nakashima-Peter Naur-John Von Neumann-Kristen Nygaard-Radia Perlman-Pier Giorgio Perotto-Rosalind Picard-Dennis Ritchie-Bertrand Russel-Claude Shannon -Masatoshi Shima-Herbert A simon-Richard Stallman-Michael Stonebreaker-Ivan Sutherland -Chai Keong Toh-An Wang-Willis Howard Ware-Maurice Wilkes -Konrad Zuse-Judea Pearl-Michael Dell-Lawrence Lessig-Andrew Ng-John Carmack-Ken Jennings-Guido Van Rossum-Seymour Ginsburg -Richard Hamming-Cuthbert Hurd-JCR licklider '''
fvpeople = vpeople.split('-')  

Very_famous = { 
'Bill Gates 1' : 'https://specials-images.forbesimg.com/imageserve/5c76b4b84bbe6f24ad99c370/416x416.jpg?background=000000&cropX1=0&cropX2=4000&cropY1=0&cropY2=4000',
'Bill Gates 2' : 'https://fm.cnbc.com/applications/cnbc.com/resources/img/editorial/2018/07/11/105322791-1531301768595gettyimages-467620670.1910x1000.jpg',
'Bill Gates 3' : 'https://bitcoinist.com/wp-content/uploads/2018/05/wiki-Bill_Gates_MSC_2017-e1525827667380.jpg',
'Steve Jobs  1' : 'https://fm.cnbc.com/applications/cnbc.com/resources/img/editorial/2013/02/26/100496736-steve-jobs-march-2011-getty.1910x1000.jpg',
'Steve Jobs  2' : 'https://images-na.ssl-images-amazon.com/images/I/61n431BDxGL.jpg',
'Steve Jobs  3' : 'https://specials-images.forbesimg.com/imageserve/5b8576db31358e0429c734e3/416x416.jpg?background=000000&cropX1=211&cropX2=2381&cropY1=900&cropY2=3072',
'Elon Musk  1' : 'https://www.biography.com/.image/t_share/MTE1ODA0OTcxOTUyMDE0ODYx/elon-musk-20837159-1-402.png',
'Elon Musk  2' : 'https://upload.wikimedia.org/wikipedia/commons/thumb/e/ed/Elon_Musk_Royal_Society.jpg/220px-Elon_Musk_Royal_Society.jpg',
'Elon Musk  3' : 'https://fm.cnbc.com/applications/cnbc.com/resources/img/editorial/2018/02/07/104994096-RTX4RL3G.1910x1000.jpg',
'Mark Zuckerberg  1' : 'https://upload.wikimedia.org/wikipedia/commons/thumb/b/b5/Mark_Zuckerberg_cropped.jpg/220px-Mark_Zuckerberg_cropped.jpg',
'Mark Zuckerberg  2' : 'https://static.independent.co.uk/s3fs-public/thumbnails/image/2019/02/01/11/mark-zuckerberg-010219.jpg',
'Mark Zuckerberg  3' : 'https://timedotcom.files.wordpress.com/2019/03/facebook-mark-zuckerberg-promises-privacy.jpg',
'Larry Page  1' : 'https://fm.cnbc.com/applications/cnbc.com/resources/img/editorial/2018/05/20/105220120-larry-page-trump-tower-entrance.530x298.jpg?v=1526932289',
'Larry Page  2' : 'https://specials-images.forbesimg.com/imageserve/5c76bcaaa7ea43100043c836/416x416.jpg?background=000000&cropX1=387&cropX2=1729&cropY1=118&cropY2=1460',
'Larry Page  3' : 'https://fm.cnbc.com/applications/cnbc.com/resources/img/editorial/2018/05/20/105220120-larry-page-trump-tower-entrance.530x298.jpg?v=1526932289',
'Sergey Brin  1' : 'https://specials-images.forbesimg.com/imageserve/5c7d7c254bbe6f78090d831f/416x416.jpg?background=000000&cropX1=884&cropX2=2499&cropY1=293&cropY2=1909',
'Sergey Brin  2' : 'https://www.biography.com/.image/ar_1:1%2Cc_fill%2Ccs_srgb%2Cg_face%2Cq_auto:good%2Cw_300/MTIwNjA4NjM0MDc3MjE4MzE2/sergey-brin-12103333-2-402.jpg',
'Sergey Brin  3' : 'https://astrumpeople.com/wp-content/uploads/2015/06/Sergey-Brin.jpg',
'Tim Berners Lee  1' : 'https://upload.wikimedia.org/wikipedia/commons/thumb/4/4e/Sir_Tim_Berners-Lee_%28cropped%29.jpg/220px-Sir_Tim_Berners-Lee_%28cropped%29.jpg',
'Tim Berners Lee  2' : 'https://static.standard.co.uk/s3fs-public/thumbnails/image/2018/03/12/08/12-03-sir-tim-berners-lee.jpg?w968',
'Tim Berners Lee  3' : 'http://qeprize.org/createthefuture/wp-content/uploads/2015/02/QEprize_EMAILRES_Jalden-0068-1024x682.jpg',
'Alan Turing  1' : 'https://www.bl.uk/britishlibrary/~/media/bl/global/whats%20on/events/2017/july/24july_alanturing.jpg',
'Alan Turing  2' : 'https://images.findagrave.com/photos250/photos/2010/157/12651680_127593467108.jpg',
'Alan Turing  3' : 'https://regmedia.co.uk/2015/05/15/alan_turing.jpg?x=442&y=293&crop=1',
'Steve Wozniak  1' : 'https://upload.wikimedia.org/wikipedia/commons/thumb/b/bf/Steve_Wozniak%2C_November_2018.jpg/220px-Steve_Wozniak%2C_November_2018.jpg',
'Steve Wozniak  2' : 'https://fm.cnbc.com/applications/cnbc.com/resources/img/editorial/2017/06/12/104524021-_Y2A6159-1.1910x1000.jpg',
'Steve Wozniak  3' : 'https://www.biography.com/.image/ar_1:1%2Cc_fill%2Ccs_srgb%2Cg_face%2Cq_auto:good%2Cw_300/MTE1ODA0OTcxODMwMDUyMzY1/stephen-wozniak-9537334-1-402.jpg',
'Linus Torvalds 1' : 'https://upload.wikimedia.org/wikipedia/commons/thumb/0/01/LinuxCon_Europe_Linus_Torvalds_03_%28cropped%29.jpg/220px-LinuxCon_Europe_Linus_Torvalds_03_%28cropped%29.jpg',
'Linus Torvalds 2' : 'https://cdn.britannica.com/99/124299-004-225EA56D.jpg',
'Linus Torvalds 3' : 'https://images.idgesg.net/images/article/2017/11/linuxcon_europe_linus_torvalds_05-100742477-large.jpg' 
    }  

Medium_famous = { 
'James Gosling  1' : 'https://images.computerhistory.org/fellows/jgosling.jpg',
'James Gosling  2' : 'http://nighthacks.com/jag/bio/JamesInViennaEnjoyingBeer.jpg',
'James Gosling  3' : 'https://upload.wikimedia.org/wikipedia/commons/thumb/1/14/James_Gosling_2008.jpg/220px-James_Gosling_2008.jpg',
'Grace Hopper  1' : 'https://upload.wikimedia.org/wikipedia/commons/a/ad/Commodore_Grace_M._Hopper%2C_USN_%28covered%29.jpg',
'Grace Hopper  2' : 'https://www.biography.com/.image/t_share/MTUxMzAzODQ1Mjk1ODI2MTEy/biography-grace-hopper.jpg',
'Grace Hopper  3' : 'https://ghc.anitab.org/wp-content/uploads/sites/2/2013/10/grace-hopper.jpg',
'Martin Hellman  1' : 'https://ee.stanford.edu/~hellman/PRphoto2016.jpg',
'Martin Hellman  2' : 'https://upload.wikimedia.org/wikipedia/commons/d/d4/Martin-Hellman.jpg',
'Martin Hellman  3' : 'https://fsi-live.s3.us-west-1.amazonaws.com/s3fs-public/staff/4812/Hellman%2C_Martin.jpeg',
'Michael Widenius  1' : 'https://upload.wikimedia.org/wikipedia/commons/6/63/Michael_%E2%80%9DMonty%E2%80%9D_Widenius_at_MariaDB%E2%80%99s_Developers_Unconference_2019_in_New_York_City_03.jpg',
'Michael Widenius  2' : 'https://www.webit.org/files/images/articles/medium/e8eec62292591f84134b8fdfccfa3209.jpeg',
'Michael Widenius  3' : 'http://ww1.prweb.com/prfiles/2009/02/10/634564/gI_0_MontyWidenius.png.jpg',
'Yukihiro Matsumoto  1' : 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/5a/Yukihiro_Matsumoto_EuRuKo_2011.jpg/220px-Yukihiro_Matsumoto_EuRuKo_2011.jpg',
'Yukihiro Matsumoto  2' : 'https://upload.wikimedia.org/wikipedia/commons/thumb/7/76/Yukihiro_Matsumoto.JPG/220px-Yukihiro_Matsumoto.JPG',
'Yukihiro Matsumoto  3' : 'https://static.lwn.net/images/conf/ks-jls-09/matz2.jpg',
'John Resig  1' : 'https://pbs.twimg.com/profile_images/1090714620275245056/HS9xcEDk_400x400.jpg',
'John Resig  2' : 'https://cdn.tutsplus.com/net/uploads/2014/03/john-resig-wide-retina-preview.jpg',
'John Resig  3' : 'http://farm3.static.flickr.com/2018/2313418303_36d49aaf24.jpg',
'Brian Kernighan  1' : 'https://www.cs.princeton.edu/~bwk/bwk.carolines.crop.jpg',
'Brian Kernighan  2' : 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/ae/Brian_Kernighan_in_2012_at_Bell_Labs_1.jpg/1200px-Brian_Kernighan_in_2012_at_Bell_Labs_1.jpg',
'Brian Kernighan  3' : 'https://artsy-media-uploads.s3.amazonaws.com/gg4GG0NinDYK_oPMGuyYoQ%2FBrian_Kernighan.jpg',
'Ken Thompson  1' : 'http://cdn.facesofopensource.com/wp-content/uploads/2017/03/23214131/faces.KenThompson20515.web_.jpg',
'Ken Thompson  2' : 'https://s24255.pcdn.co/wp-content/uploads/2015/10/thompson01.jpg',
'Ken Thompson  3' : 'http://en.chessbase.com/portals/4/files/news/2011/thompson09.jpg',
'David Axmark  1' : 'https://upload.wikimedia.org/wikipedia/commons/5/55/David_Axmark.jpg',
'David Axmark  2' : 'https://res-3.cloudinary.com/crunchbase-production/image/upload/c_thumb,h_256,w_256,f_auto,g_faces,z_0.7,q_auto:eco/v1468669217/wbbkx8huaapy3e5rzmil.png',
'David Axmark  3' : 'https://upload.wikimedia.org/wikipedia/commons/b/b8/David_Axmark_at_MySQL_Conference_05.jpg',
'Ben Goodger  1' : 'https://upload.wikimedia.org/wikipedia/commons/9/96/Ben_Goodger.png',
'Ben Goodger  2' : 'https://thimbleprojects.org/ghumphreyevans/290024/Ben%20Goodger.jpg',
'Ben Goodger  3' : 'https://thimbleprojects.org/ghumphreyevans/290024/Ben%20Goodger3.jpg',
'Larry Wall  1' : 'https://upload.wikimedia.org/wikipedia/commons/thumb/b/b3/Larry_Wall_YAPC_2007.jpg/220px-Larry_Wall_YAPC_2007.jpg',
'Larry Wall  2' : 'http://cdn.facesofopensource.com/wp-content/uploads/2017/03/19223323/larrywall.faces23418.web_.jpg',
'Larry Wall  3' : 'https://www.evozon.com/wp-content/uploads/2016/12/larrywall.png',
'Bjarne Stroustrup  1' : 'https://upload.wikimedia.org/wikipedia/commons/thumb/0/0e/Bjarne-stroustrup_%28cropped%29.jpg/220px-Bjarne-stroustrup_%28cropped%29.jpg',
'Bjarne Stroustrup  2' : 'https://images.computerhistory.org/fellows/2015_bjarne_straustroup.jpg',
'Bjarne Stroustrup  3' : 'https://usesthis.com/images/interviews/bjarne.stroustrup/portrait.jpg',
'Rasmus Lerdorf  1' : 'https://pbs.twimg.com/profile_images/918348833205116928/V9ROYRNJ_400x400.jpg',
'Rasmus Lerdorf  2' : 'https://upload.wikimedia.org/wikipedia/commons/thumb/6/66/Rasmus_Lerdorf_August_2014_%28cropped%29.JPG/1200px-Rasmus_Lerdorf_August_2014_%28cropped%29.JPG',
'Rasmus Lerdorf  3' : 'https://upload.wikimedia.org/wikipedia/commons/thumb/3/33/Wikirl.jpg/250px-Wikirl.jpg',
'Niklaus Wirth  1' : 'https://upload.wikimedia.org/wikipedia/commons/4/49/Niklaus_Wirth%2C_UrGU.jpg',
'Niklaus Wirth  2' : 'https://images.computerhistory.org/fellows/2004_niklaus_wirth.jpg',
'Niklaus Wirth  3' : 'https://www.thocp.net/biographies/pictures/wirth_niklaus.jpg',
'shigeru miyamoto 1' : 'https://m.media-amazon.com/images/M/MV5BYTViMTA1MzEtODgyZi00YmM2LTgzMjAtYTgxN2JiYjZlNzc4XkEyXkFqcGdeQXVyMzM4MjM0Nzg@._V1_UY317_CR76,0,214,317_AL_.jpg',
'shigeru miyamoto 2' : 'https://cdn1.thr.com/sites/default/files/imagecache/scale_crop_768_433/2018/08/gettyimages-628640766-h_2018.jpg',
'shigeru miyamoto 3' : 'https://thumbor.forbes.com/thumbor/1280x868/https%3A%2F%2Fblogs-images.forbes.com%2Folliebarder%2Ffiles%2F2016%2F09%2Fmario64_miyamoto-1200x675.jpg', 
    }  

Low_famous = { 
'Howard Aiken 1' : 'https://upload.wikimedia.org/wikipedia/commons/c/c9/Aiken.jpeg',
'Howard Aiken 2' : 'https://history-computer.com/ModernComputer/Relays/images/AikenPortrait3.jpg',
'Howard Aiken 3' : 'https://ethw.org/w/images/8/8b/Aiken.jpg',
'Frances E Allen 1' : 'https://upload.wikimedia.org/wikipedia/commons/1/15/Allen_mg_2528-3750K-b.jpg',
'Frances E Allen 2' : 'http://deliveryimages.acm.org/10.1145/1870000/1866752/figs/uf1.jpg',
'Frances E Allen 3' : 'https://www.berkeley.edu/news/berkeleyan/2008/01/images/franallen1.jpg',
'John Atanasoff 1' : 'https://history-computer.com/ModernComputer/Electronic/Images/AtanasoffPortrait.jpg',
'John Atanasoff 2' : 'https://www.biography.com/.image/t_share/MTI2NzY4NDY0NzgxMTY2NjAy/john-atanasoff-wikicommonsjpg.jpg',
'John Atanasoff 3' : 'https://history.computer.org/pioneers/images/atanasoff.jpg',
'Charles Babbage1' : 'https://upload.wikimedia.org/wikipedia/commons/thumb/6/6b/Charles_Babbage_-_1860.jpg/220px-Charles_Babbage_-_1860.jpg',
'Charles Babbage2' : 'https://upload.wikimedia.org/wikipedia/commons/thumb/4/44/Charles_Babbage_by_Antoine_Claudet_c1847-51-crop.jpg/170px-Charles_Babbage_by_Antoine_Claudet_c1847-51-crop.jpg',
'Charles Babbage3' : 'http://www.5minutebiographies.com/wp-content/uploads/2016/12/charles-babbage-899x492.jpg',
'John Backus1' : 'https://upload.wikimedia.org/wikipedia/commons/thumb/b/b2/John_Backus_2.jpg/220px-John_Backus_2.jpg',
'John Backus2' : 'https://ethw.org/w/images/5/57/Backus.jpg',
'John Backus3' : 'https://images.computerhistory.org/fellows/1997_john_backus.jpg',
'Corrado bohm1' : 'http://www.corradobohm.it/Corrado_Bohm/Home_files/shapeimage_3.png',
'Corrado bohm2' : 'http://www.corradobohm.it/Corrado_Bohm/Crete1_files/P0001563.jpg',
'Corrado bohm3' : 'https://www.macitynet.it/wp-content/uploads/2017/10/Corrado-Bohm-1.jpg',
'Fred Brooks1' : 'https://upload.wikimedia.org/wikipedia/commons/thumb/9/91/Fred_Brooks.jpg/220px-Fred_Brooks.jpg',
'Fred Brooks2' : 'https://www.seas.harvard.edu/sites/default/files/images/oldsite/Fred-Brooks.jpg',
'Fred Brooks3' : 'https://www.azquotes.com/public/pictures/authors/49/c5/49c51079aedb134582fdcb691b62af61/5405afc19b3e0_fred_brooks.jpg',
'Vannevar Bush1' : 'https://upload.wikimedia.org/wikipedia/commons/thumb/e/ea/Vannevar_Bush_portrait.jpg/300px-Vannevar_Bush_portrait.jpg',
'Vannevar Bush2' : 'https://www.atomicheritage.org/sites/default/files/vannevar-bush-1-sized.jpg',
'Vannevar Bush3' : 'https://www.i-programmer.info/images/stories/News/2011/MARCH/bush3_lg.jpg',
'Vint Cerf1' : 'http://photos.geni.com/p13/05/27/44/f5/53444848551e4ad0/vint_cerf_final1353-1_1_1__original.jpg',
'Vint Cerf2' : 'https://upload.wikimedia.org/wikipedia/commons/thumb/b/bb/Vint_Cerf_-_2010.jpg/260px-Vint_Cerf_-_2010.jpg',
'Vint Cerf3' : 'https://amp.businessinsider.com/images/5c424f082bdd7f04785cf397-750-563.jpg',
'Noam Chomsky1' : 'https://truthout.org/wp-content/uploads/2018/08/GettyImages-550172113-1200x800.jpg',
'Noam Chomsky2' : 'https://pbs.twimg.com/profile_images/880114944645242885/h6UI6Iq1_400x400.jpg',
'Noam Chomsky3' : 'https://cdn.britannica.com/11/198711-004-D24BFB08.jpg',
'Edmund Clarke1' : 'https://www.cs.cmu.edu/~emc/images/EMC%20Photo%202013.jpg',
'Edmund Clarke2' : 'https://www.eurekalert.org/multimedia/pub/web/6733_web.jpg',
'Edmund Clarke3' : 'https://www.cs.cmu.edu/sites/default/files/styles/news_item_image/public/edmund-clarke.jpg?itok=nMerAKd8',
'Lynn Conway 1' : 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/50/Lynn_Conway_July_2006.jpg/200px-Lynn_Conway_July_2006.jpg',
'Lynn Conway 2' : 'http://www.eecs.umich.edu/eecs/about/articles/2014/conway_banner.jpg',
'Lynn Conway 3' : 'https://alchetron.com/cdn/lynn-conway-603da613-77eb-4732-a62c-65bca7a2a58-resize-750.jpeg',
'Stephen Cook1' : 'http://www.cs.toronto.edu/~sacook/Steve_by_Yvonne.04.JPG',
'Stephen Cook2' : 'https://upload.wikimedia.org/wikipedia/commons/thumb/6/68/Prof.Cook.jpg/220px-Prof.Cook.jpg',
'Stephen Cook3' : 'http://news.artsci.utoronto.ca/wp-content/uploads/2016/01/s-cook-1-300x181.jpg',
'Edsger Dijkstra 1' : 'https://upload.wikimedia.org/wikipedia/commons/d/d9/Edsger_Wybe_Dijkstra.jpg',
'Edsger Dijkstra 2' : 'https://www.thocp.net/biographies/pictures/dijkstra_edgar1.jpg',
'Edsger Dijkstra 3' : 'https://i.ytimg.com/vi/ExDsgb_0s-w/hqdefault.jpg',
'Ernest Allen Emerson 1' : 'http://www.cs.utexas.edu/~emerson/eae.c.2002.small.jpg',
'Ernest Allen Emerson 2' : 'https://www.ecured.cu/images/thumb/0/09/E.AllenEmerson.jpg/260px-E.AllenEmerson.jpg',
'Ernest Allen Emerson 3' : 'https://www.heidelberg-laureate-forum.org/wp-content/uploads/2013/05/Emerson-E.-Allen-460x306.jpg',
'Douglas Engelbart1' : 'https://upload.wikimedia.org/wikipedia/commons/thumb/7/78/Douglas_Engelbart_in_2008.jpg/220px-Douglas_Engelbart_in_2008.jpg',
'Douglas Engelbart2' : 'https://www.sri.com/sites/default/files/uploads/douglas_engelbart_and_mouse.jpg',
'Douglas Engelbart3' : 'https://engineering.oregonstate.edu/sites/engineering.oregonstate.edu/files/images/stater-awards/engelbart.jpg',
'Federico Faggin1' : 'https://upload.wikimedia.org/wikipedia/commons/thumb/f/fc/Federico_Faggin_%28cropped%29.jpg/220px-Federico_Faggin_%28cropped%29.jpg',
'Federico Faggin2' : 'https://images.computerhistory.org/fellows/2009_federico_faggin.jpg',
'Federico Faggin3' : 'http://www.fagginfoundation.org/wp-content/uploads/2014/08/federico-faggin-1972.png',
'Elizabeth Feinler1' : 'https://upload.wikimedia.org/wikipedia/commons/thumb/6/6d/ElizabethFeinler-2011.jpg/220px-ElizabethFeinler-2011.jpg',
'Elizabeth Feinler2' : 'https://media.wired.com/photos/5932e15158b0d64bb35d3c69/master/pass/jake-feinler.jpg',
'Elizabeth Feinler3' : 'https://www.internethalloffame.org/sites/default/files/inductees/Feinler%20Grayscale_1.jpg',
'Tommy Flowers1' : 'https://upload.wikimedia.org/wikipedia/commons/thumb/8/84/Tommy_Flowers.jpg/220px-Tommy_Flowers.jpg',
'Tommy Flowers2' : 'http://home.bt.com/images/who-is-tommy-flowers-136425504966302601-180301155256.jpg',
'Tommy Flowers3' : 'https://spartacus-educational.com/00FlowersT1.jpg',
'Sally Floyd1' : 'https://www.icir.org/floyd/images/sfsunflowers1.jpg',
'Sally Floyd2' : 'https://www.icsi.berkeley.edu/icsi/sites/default/files/staff_photos/floyd.JPG',
'Sally Floyd3' : 'https://science-match.tagesspiegel.de/system/images/820/medium/49_Floyd.jpg',
'Charles Sanders Pierce1' : 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/58/Charles_Sanders_Peirce.jpg/220px-Charles_Sanders_Peirce.jpg',
'Charles Sanders Pierce2' : 'https://cdn.britannica.com/04/127704-004-3163A0E3.jpg',
'Charles Sanders Pierce3' : 'http://blogs.law.harvard.edu/houghtonmodern/files/2013/08/Peirce-234x300.jpg',
'Stephen Furber1' : 'https://upload.wikimedia.org/wikipedia/commons/thumb/3/33/Steve_Furber.jpg/200px-Steve_Furber.jpg',
'Stephen Furber2' : 'http://www.anglia.ac.uk/-/media/Images/Honoraries/Honorary-photos/234x234/Steven-Furber_234x234.jpg',
'Stephen Furber3' : 'http://www.cs.manchester.ac.uk/media/eps/schoolofcomputerscience/research/groups/Steve-furber.jpg',
'Sophie Wilson1' : 'https://upload.wikimedia.org/wikipedia/commons/b/b3/Sophie_Wilson.jpg',
'Sophie Wilson2' : 'https://regmedia.co.uk/2012/04/24/sw_1.jpg',
'Sophie Wilson3' : 'http://www.computinghistory.org.uk/userdata/images/large/29/59/product-72959.jpg',
'Seymour Ginsburg1' : 'https://gurdjieffbooks.files.wordpress.com/2011/01/gurdjieff2.jpg',
'Seymour Ginsburg2' : 'https://www.gurusfeet.com/files/imagecache/guru_pic_main_imagescale/files/gurus_pics/gurdjieff.jpg',
'Seymour Ginsburg3' : 'https://highgradediscourse.files.wordpress.com/2014/03/gurdjieff1.jpg?w=630',
'Susan L graham1' : 'https://www.ithistory.org/sites/default/files/honor-roll/Susan%20L.%20Graham.jpg',
'Susan L graham2' : 'http://people.eecs.berkeley.edu/~graham/images/SLG1jpg.jpeg',
'Susan L graham3' : 'https://i.ytimg.com/vi/Lky2bcz9Xnc/maxresdefault.jpg',
'Jim Gray1' : 'https://images.findagrave.com/photos/2010/12/46648590_126343570647.jpg',
'Jim Gray2' : 'https://upload.wikimedia.org/wikipedia/commons/thumb/7/76/Jim_Gray_Computing_in_the_21st_Century_2006.jpg/220px-Jim_Gray_Computing_in_the_21st_Century_2006.jpg',
'Jim Gray3' : 'http://res.sys-con.com/story/mar12/2202529/Jim%20Gray_0.jpg',
'Barbara Grosz1' : 'https://grosz.seas.harvard.edu/files/styles/os_files_medium/public/grosz/files/grosz_headshot.jpeg',
'Barbara Grosz2' : 'https://www.seas.harvard.edu/sites/default/files/images/news/Barbara700.jpg',
'Barbara Grosz3' : 'https://www.radcliffe.harvard.edu/sites/radcliffe.harvard.edu/files/Images/About_Us/barbara-grosz_photo-by-asia-kepka_350px.jpg',
'Margaret Hamilton1' : 'https://upload.wikimedia.org/wikipedia/commons/d/db/Margaret_Hamilton_-_restoration.jpg',
'Margaret Hamilton2' : 'https://upload.wikimedia.org/wikipedia/commons/thumb/6/68/Margaret_Hamilton_1995.jpg/220px-Margaret_Hamilton_1995.jpg',
'Margaret Hamilton3' : 'https://upload.wikimedia.org/wikipedia/commons/thumb/6/63/Margaret_Hamilton_1989.jpg/180px-Margaret_Hamilton_1989.jpg',
'Geoffrey Hinton1' : 'https://www.utoronto.ca/sites/default/files/2016-12-05-geoffrey-hinton.jpg',
'Geoffrey Hinton2' : 'https://images.thestar.com/wgf2KXhd5xhhKyMIEk-VAXShecA=/1200x799/smart/filters:cb(2700061000)/https://www.thestar.com/content/dam/thestar/news/world/2015/04/17/how-a-toronto-professors-research-revolutionized-artificial-intelligence/geoffrey-hinton-3.jpg',
'Geoffrey Hinton3' : 'http://www.cs.toronto.edu/~hinton/geoff7.jpg',
'Charles Anthony Richard Hoare 1' : 'https://upload.wikimedia.org/wikipedia/commons/2/2c/Sir_Tony_Hoare_IMG_5125.jpg',
'Charles Anthony Richard Hoare 2' : 'https://upload.wikimedia.org/wikipedia/commons/thumb/f/fe/Hoare.jpg/225px-Hoare.jpg',
'Charles Anthony Richard Hoare 3' : 'https://i.ytimg.com/vi/duEkPC7OuoQ/maxresdefault.jpg',
'Betty Holberton1' : 'https://ethw.org/w/images/thumb/4/4a/Betty-1944-loeb.jpg/300px-Betty-1944-loeb.jpg',
'Betty Holberton2' : 'https://3.bp.blogspot.com/-AcnRyDiLPWs/WcypxnE_XHI/AAAAAAAAnKI/ikmpyYe7c94Mgv59v2p1OnI4Mqf_Y1OegCLcBGAs/w1200-h630-p-k-no-nu/Holberton.png',
'Betty Holberton3' : 'https://mujeresconciencia.com/app/uploads/2015/03/betty_holberton-300x168.jpg',
'Harry Huskey1' : 'https://upload.wikimedia.org/wikipedia/commons/thumb/b/b2/Harry_Huskey_2011.jpg/220px-Harry_Huskey_2011.jpg',
'Harry Huskey2' : 'https://news.ucsc.edu/2017/04/images/harry-huskey-1-350.jpg',
'Harry Huskey3' : 'http://s386083476.onlinehome.us/wp-content/uploads/2017/05/HDH05.jpg',
'Kenneth Iverson1' : 'https://upload.wikimedia.org/wikipedia/en/3/38/Kei_younger.jpg',
'Kenneth Iverson2' : 'https://amturing.acm.org/images/lg_aw/9147499.jpg',
'Kenneth Iverson3' : 'http://www.britishaplassociation.co.uk/wp-content/uploads/2016/06/blog-who-was-ken-iverson.jpg',
'Karen Sparck Jones1' : 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/af/Karen_Sp%C3%A4rck.jpg/220px-Karen_Sp%C3%A4rck.jpg',
'Karen Sparck Jones2' : 'https://www.cl.cam.ac.uk/misc/obituaries/sparck-jones/video/award-lecture-2007.jpg',
'Karen Sparck Jones3' : 'https://i.ytimg.com/vi/5fYeKiebpuo/hqdefault.jpg',
'Jacek Karpinski 1' : 'https://upload.wikimedia.org/wikipedia/commons/thumb/f/f5/Jacek_Karpi%C5%84ski.jpg/220px-Jacek_Karpi%C5%84ski.jpg',
'Jacek Karpinski 2' : 'http://api.culture.pl/sites/default/files/images/imported/_a%20culture%20english/history/JacekKarpinski/karpinski1_forum.jpg',
'Jacek Karpinski 3' : 'http://www.spkalwaria.iap.pl/baza/strony/projekt_pawlik_balus/jacek3.jpg',
'Alan Kay1' : 'https://upload.wikimedia.org/wikipedia/commons/thumb/7/76/Alan_Kay_%283097597186%29.jpg/1200px-Alan_Kay_%283097597186%29.jpg',
'Alan Kay2' : 'https://history-computer.com/ModernComputer/Personal/images/alan_kay.jpg',
'Alan Kay3' : 'https://i.ytimg.com/vi/KVUGkuUj28o/maxresdefault.jpg',
'Stephen Cole Kleene1' : 'https://upload.wikimedia.org/wikipedia/commons/thumb/1/1c/Kleene.jpg/220px-Kleene.jpg',
'Stephen Cole Kleene2' : 'https://www.nap.edu/openbook/0309062950/xhtml/images/20003286015401.jpg',
'Stephen Cole Kleene3' : 'http://aseelghazal.weebly.com/uploads/4/0/4/5/40450643/1420531277.png',
'Donald Knuth1' : 'https://upload.wikimedia.org/wikipedia/commons/4/4f/KnuthAtOpenContentAlliance.jpg',
'Donald Knuth2' : 'https://amp.businessinsider.com/images/55a003fb6bb3f7996df7425c-750-500.jpg',
'Donald Knuth3' : 'https://i.ytimg.com/vi/g4lhrVPDUG0/maxresdefault.jpg',
'Leslie Lamport1' : 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/50/Leslie_Lamport.jpg/220px-Leslie_Lamport.jpg',
'Leslie Lamport2' : 'https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/Headshot__0087_cropped_leslie-lamport.jpg',
'Leslie Lamport3' : 'https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/acm-reviews-the-achievements-of-leslie-lamport-1-480x280.jpg',
'Barbara Liskov1' : 'https://upload.wikimedia.org/wikipedia/commons/thumb/3/38/Barbara_Liskov_MIT_computer_scientist_2010.jpg/220px-Barbara_Liskov_MIT_computer_scientist_2010.jpg',
'Barbara Liskov2' : 'https://amturing.acm.org/images/lg_aw/1108679.jpg',
'Barbara Liskov3' : 'https://www.heidelberg-laureate-forum.org/wp-content/uploads/2016/09/liskov_new-460x305.jpg',
'Ada Lovelace1' : 'https://upload.wikimedia.org/wikipedia/commons/a/a4/Ada_Lovelace_portrait.jpg',
'Ada Lovelace2' : 'https://upload.wikimedia.org/wikipedia/commons/thumb/8/87/Ada_Lovelace.jpg/220px-Ada_Lovelace.jpg',
'Ada Lovelace3' : 'http://www.claymath.org/sites/default/files/ada_lovelace.jpeg',
'John McCarthy1' : 'https://upload.wikimedia.org/wikipedia/commons/4/49/John_McCarthy_Stanford.jpg',
'John McCarthy2' : 'https://ichef.bbci.co.uk/news/304/media/images/56264000/jpg/_56264826_johnmccarthy1.jpg',
'John McCarthy3' : 'https://www.singularityweblog.com/wp-content/uploads/2018/08/John-McCarthy.jpg',
'Marvin Minsky1' : 'https://upload.wikimedia.org/wikipedia/commons/thumb/2/28/Marvin_Minsky_at_OLPCb.jpg/220px-Marvin_Minsky_at_OLPCb.jpg',
'Marvin Minsky2' : 'http://www.kurzweilai.net/images/Marvin-Minksy-PhD-B3.png',
'Marvin Minsky3' : 'https://media.wired.com/photos/59273a19ac01987bf0138dec/master/pass/marvin-minsky-bot-D0M7FA.jpg',
'Yoshiro Nakamatsu1' : 'https://upload.wikimedia.org/wikipedia/commons/thumb/b/bd/Nakamatsu.jpg/220px-Nakamatsu.jpg',
'Yoshiro Nakamatsu2' : 'https://cdn.japantimes.2xx.jp/wp-content/uploads/2014/06/p2-nakamatsu-a-20140628.jpg',
'Yoshiro Nakamatsu3' : 'http://evolution.skf.com/wp-content/uploads/2002/09/Yoshiro-Nakamatsu2.jpg',
'Gottfried Leibniz 1' : 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/ce/Gottfried_Wilhelm_Leibniz%2C_Bernhard_Christoph_Francke.jpg/220px-Gottfried_Wilhelm_Leibniz%2C_Bernhard_Christoph_Francke.jpg',
'Gottfried Leibniz 2' : 'https://www.iep.utm.edu/wp-content/media/leibniz.jpg',
'Gottfried Leibniz 3' : 'https://imgc.allpostersimages.com/img/print/posters/sheila-terry-gottfried-leibniz-german-mathematician_a-G-10023072-4989915.jpg',
'Peter Naur1' : 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/55/Peternaur.JPG/200px-Peternaur.JPG',
'Peter Naur2' : 'https://www.heidelberg-laureate-forum.org/wp-content/uploads/2013/05/Naur.jpg',
'Peter Naur3' : 'http://www.scilogs.com/hlf/wp-content/blogs.dir/132/files/HLF2015_Friday002_cf.jpg',
'John Von Neumann1' : 'https://cdn.dotcom.sothebys.psdops.com/dims4/default/5e54f82/2147483647/strip/true/crop/728x957+0+0/resize/684x899!/quality/90/?url=https%3A%2F%2Fcdn.dotcom.sothebys.psdops.com%2F18%2F93%2F859d7a4f43de93f54b8f4dd76d7c%2F1251l18409-9w98j.jpg',
'John Von Neumann2' : 'https://upload.wikimedia.org/wikipedia/commons/thumb/7/78/HD.3F.191_%2811239892036%29.jpg/220px-HD.3F.191_%2811239892036%29.jpg',
'John Von Neumann3' : 'https://todayinsci.com/V/VonNeumann_John/VonNeumannJohn300px.jpg',
'Kristen Nygaard1' : 'http://heim.ifi.uio.no/~gisle/in_memoriam_kristen/images/kristen04w.jpg',
'Kristen Nygaard2' : 'https://upload.wikimedia.org/wikipedia/commons/b/bb/Kristen-Nygaard-SBLP-1997-head.png',
'Kristen Nygaard3' : 'https://media.snl.no/system/images/31355/standard_kristen-nygaard.jpg',
'Radia Perlman1' : 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/af/Radia_Perlman_2009.jpg/220px-Radia_Perlman_2009.jpg',
'Radia Perlman2' : 'https://www.internethalloffame.org/sites/default/files/inductees/radia_perlman.jpg',
'Radia Perlman3' : 'http://simplecore.intel.com/newsroom/wp-content/uploads/sites/11/2011/04/Radia-Perlman-244x300.png',
'Pier Giorgio Perotto1' : 'https://i.pinimg.com/originals/11/ce/fe/11cefebcd69806a878826e4bd2041c2c.jpg',
'Pier Giorgio Perotto2' : 'http://www.apogeonline.com/2002/webzine/01/28/06/20020128060101.jpg',
'Pier Giorgio Perotto3' : 'https://i.ytimg.com/vi/ZTDmerqIsJs/maxresdefault.jpg',
'Rosalind Picard1' : 'http://web.media.mit.edu/~picard/img/Picard-credit-A-Ryan.png',
'Rosalind Picard2' : 'https://pbs.twimg.com/profile_images/423189890545643520/w6Fjk14f_400x400.png',
'Rosalind Picard3' : 'https://futureofstorytelling.org/uploads/speaker/card/Picard%20-%20photo.jpg',
'Dennis Ritchie1' : 'https://upload.wikimedia.org/wikipedia/commons/thumb/2/23/Dennis_Ritchie_2011.jpg/220px-Dennis_Ritchie_2011.jpg',
'Dennis Ritchie2' : 'https://cdn-images-1.medium.com/max/1000/1*4AApxPkF4yXzY0jF0yHgkA.jpeg',
'Dennis Ritchie3' : 'https://ethw.org/w/images/thumb/9/97/Dennis_M._Ritchie_2260.jpg/300px-Dennis_M._Ritchie_2260.jpg',
'Bertrand Russel1' : 'https://www.the-tls.co.uk/s3/tls-prod/uploads/2018/10/Russell.jpg',
'Bertrand Russel2' : 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/5f/Bertrand_Russell_1957.jpg/220px-Bertrand_Russell_1957.jpg',
'Bertrand Russel3' : 'https://www.bbvaopenmind.com/wp-content/uploads/2017/05/Bertrandrussell-xlarge_trans.jpeg',
'Claude Shannon 1' : 'https://media.newyorker.com/photos/5909765cc14b3c606c1089f4/master/w_727,c_limit/Roberts-Claude-Shannon.jpg',
'Claude Shannon 2' : 'http://theinstitute.ieee.org/image/MTM1ODQ0.jpeg',
'Claude Shannon 3' : 'https://history-computer.com/ModernComputer/thinkers/images/shannon.jpg',
'Masatoshi Shima1' : 'https://images.computerhistory.org/fellows/2009_masatoshi_shima.jpg',
'Masatoshi Shima2' : 'https://upload.wikimedia.org/wikipedia/commons/thumb/e/e2/Masatoshi_Shima.jpg/220px-Masatoshi_Shima.jpg',
'Masatoshi Shima3' : 'https://ethw.org/w/images/thumb/5/50/2138_-_Masatoshi_Shima.jpg/300px-2138_-_Masatoshi_Shima.jpg',
'Herbert A simon1' : 'https://www.nobelprize.org/images/simon-13300-portrait-medium.jpg',
'Herbert A simon2' : 'https://www.cmu.edu/simon/images/herbertsimon2.jpg',
'Herbert A simon3' : 'https://www.econlib.org/wp-content/uploads/2018/02/223-herbert-a-simon.jpg',
'Richard Stallman1' : 'https://upload.wikimedia.org/wikipedia/commons/thumb/7/7b/Richard_Stallman_-_F%C3%AAte_de_l%27Humanit%C3%A9_2014_-_010.jpg/220px-Richard_Stallman_-_F%C3%AAte_de_l%27Humanit%C3%A9_2014_-_010.jpg',
'Richard Stallman2' : 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/50/Richard_M_Stallman_Swathanthra_2014_kerala.jpg/220px-Richard_M_Stallman_Swathanthra_2014_kerala.jpg',
'Richard Stallman3' : 'https://static.fsf.org/nosvn/rms-photos/20161122-pamplona/20161122-pamplona-11.jpg',
'Michael Stonebreaker1' : 'https://www.acm.org/binaries/content/gallery/acm/ctas/people/michael-stonebraker.jpg/michael-stonebraker.jpg/acm%3Adesktopcta',
'Michael Stonebreaker2' : 'https://www.csail.mit.edu/sites/default/files/styles/headshot/public/images/migration/stonebraker.jpg?h=5636fc5d&itok=a6jqPUh2',
'Michael Stonebreaker3' : 'https://proprofs.com/quiz-school/topic_images/p1bahkh2b613t81odou61bv1cbu3.jpg',
'Ivan Sutherland 1' : 'https://www.heidelberg-laureate-forum.org/wp-content/uploads/2013/05/Sutherland-Ivan-460x306.jpg',
'Ivan Sutherland 2' : 'https://upload.wikimedia.org/wikipedia/commons/5/5c/Ivan_Sutherland_at_CHM.jpg',
'Ivan Sutherland 3' : 'https://amturing.acm.org/images/lg_aw/3467412.jpg',
'Chai Keong Toh1' : 'https://ethw.org/w/images/1/12/Prof_toh_2016.jpg',
'Chai Keong Toh2' : 'https://www.imda.gov.sg/-/media/imda/images/inner/infocomm-and-media-buzz/images/smart-nation/2015/june/100615_iot_main.jpg',
'Chai Keong Toh3' : 'https://upload.wikimedia.org/wikipedia/commons/thumb/1/1b/Chai_K_Toh.JPG/1200px-Chai_K_Toh.JPG',
'An Wang1' : 'https://www.thefamouspeople.com/profiles/thumbs/an-wang-1.jpg',
'An Wang2' : 'https://www.i-programmer.info/images/stories/ComputerCreators/Wang/awang.jpg',
'An Wang3' : 'https://www.notablebiographies.com/images/uewb_10_img0711.jpg',
'Willis Howard Ware1' : 'https://history.computer.org/pioneers/images/ware.jpg',
'Willis Howard Ware2' : 'https://static01.nyt.com/images/2013/12/03/business/WARE-obit/WARE-obit-articleLarge.jpg?quality=75&auto=webp&disable=upscale',
'Willis Howard Ware3' : 'https://epic.org/misc/ware/ware.jpg',
'Maurice Wilkes 1' : 'https://upload.wikimedia.org/wikipedia/commons/thumb/7/74/Maurice_Vincent_Wilkes_1980_%283%29.jpg/1200px-Maurice_Vincent_Wilkes_1980_%283%29.jpg',
'Maurice Wilkes 2' : 'https://secure.i.telegraph.co.uk/multimedia/archive/01774/maurice-wilkes_1774781b.jpg',
'Maurice Wilkes 3' : 'https://www.cl.cam.ac.uk/misc/obituaries/wilkes/mvw.jpg',
'Konrad Zuse1' : 'https://upload.wikimedia.org/wikipedia/commons/thumb/d/da/Konrad_Zuse_%281992%29.jpg/220px-Konrad_Zuse_%281992%29.jpg',
'Konrad Zuse2' : 'https://images.computerhistory.org/fellows/1999_konrad_zuse.jpg',
'Konrad Zuse3' : 'https://sourceforge.net/blog/wp-content/uploads/2018/04/konrad-zuse-big.jpg',
'Judea Pearl1' : 'https://pbs.twimg.com/profile_images/1012181647993606144/TeYvs7NH_400x400.jpg',
'Judea Pearl2' : 'http://bayes.cs.ucla.edu/jp-bw-photo72dpi.jpg',
'Judea Pearl3' : 'http://www.danielpearl.org/wp-content/uploads/2014/03/Judea_Pearl.jpg',
'Michael Dell1' : 'https://fm.cnbc.com/applications/cnbc.com/resources/img/editorial/2017/01/19/104228474-_95A5274.1910x1000.JPG?v=1484839063',
'Michael Dell2' : 'https://specials-images.forbesimg.com/imageserve/5c756bce31358e35dd275332/416x416.jpg?background=000000&cropX1=1473&cropX2=5110&cropY1=0&cropY2=3634',
'Michael Dell3' : 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/ce/Michael_Dell_2010.jpg/220px-Michael_Dell_2010.jpg',
'Lawrence Lessig1' : 'https://upload.wikimedia.org/wikipedia/commons/thumb/9/91/Lawrence_Lessig_May_2017.jpg/220px-Lawrence_Lessig_May_2017.jpg',
'Lawrence Lessig2' : 'http://www.lessig.org/wp-content/uploads/2012/06/lessig_desk_2.jpg',
'Lawrence Lessig3' : 'http://www.law.harvard.edu/faculty/pictures/10519.jpg',
'Andrew Ng1' : 'https://pbs.twimg.com/profile_images/733174243714682880/oyG30NEH_400x400.jpg',
'Andrew Ng2' : 'https://supchina.com/wp-content/uploads/2016/09/ANDREW-NG.png',
'Andrew Ng3' : 'https://venturebeat.com/wp-content/uploads/2017/08/2017-07-28_coursera_092117.jpg?fit=400%2C267&strip=all',
'John Carmack1' : 'https://upload.wikimedia.org/wikipedia/commons/thumb/d/dc/John_Carmack_GDC_2010.jpg/220px-John_Carmack_GDC_2010.jpg',
'John Carmack2' : 'https://cdn.uploadvr.com/wp-content/uploads/2017/02/john-carmack-featured-1024x683.jpg',
'John Carmack3' : 'http://www.bafta.org/sites/default/files/styles/news_main/public/externals/69827f740e5eb76041a52b02ee7cb1da.jpg?itok=YEy3DXak',
'Ken Jennings1' : 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/af/Ken_Jennings_cropped_retouched.jpg/200px-Ken_Jennings_cropped_retouched.jpg',
'Ken Jennings2' : 'https://pixel.nymag.com/imgs/daily/vulture/2019/03/06/06-ken-jennings-all-star-games.w330.h412.jpg',
'Ken Jennings3' : 'https://pbs.twimg.com/profile_images/1093953474562150401/CQUhkQHz_400x400.jpg',
'Guido Van Rossum1' : 'https://upload.wikimedia.org/wikipedia/commons/thumb/d/d0/Guido-portrait-2014-curvves.jpg/290px-Guido-portrait-2014-curvves.jpg',
'Guido Van Rossum2' : 'https://pbs.twimg.com/profile_images/424495004/GuidoAvatar_400x400.jpg',
'Guido Van Rossum3' : 'https://www.theinquirer.net/w-images/7499c686-9928-4863-adb9-1c9f5fcec802/1/guidovanrossumpython-580x358.jpg',
'joseph carl robnett licklider 1' : 'https://history-computer.com/Internet/images/licklider.jpg',
'joseph carl robnett licklider 2' : 'https://www.internethalloffame.org/sites/default/files/inductees/jcr%20licklider.jpg',
'joseph carl robnett licklider 3' : 'https://i.pinimg.com/originals/bc/5e/00/bc5e00507fdb75d2a879f6d5f210c0cc.jpg',
'Richard Hamming1' : 'https://upload.wikimedia.org/wikipedia/en/thumb/0/08/Richard_Hamming.jpg/220px-Richard_Hamming.jpg',
'Richard Hamming2' : 'https://ethw.org/w/images/thumb/4/4f/Richard_Hamming_1598.jpg/300px-Richard_Hamming_1598.jpg',
'Richard Hamming3' : 'https://cdn.lifehack.org/wp-content/uploads/2014/10/hamming-4.jpg',
'Cuthbert Hurd1' : 'https://ethw.org/w/images/a/ac/180px-Cuthbert_Hurd.jpg',
'Cuthbert Hurd2' : 'https://www.ibm.com/ibm/history/ibm100/images/icp/P687534R06483O94/us__none__ibm100__cult_innovation__james_w_bryce__140x175.jpg',
'Cuthbert Hurd3' : 'https://images.computerhistory.org/tdih/05april-1.jpg?w=600',
'ramon llull 1' : 'https://upload.wikimedia.org/wikipedia/commons/thumb/0/04/Ramon_Llull.jpg/220px-Ramon_Llull.jpg',
'ramon llull 2' : 'https://qpr2l7.imagenii.com/static1.seemallorca.com/image_uploader/photos/b7/large/ramon-llull-father-of-the-catalan-language-663.jpg?f=q(v=.8)&auth=e2f306e830961023a1b15f18371d172a7d8cd18e',
'ramon llull 3' : 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRHF_Pzci-anl6lw88OHns56O6AdxWa9zHewjnlBOj9n1KZGOOM',
 
    }  

subscription_key = "71ad32482bbb4d99a0882c34d8b08d9f"
  

headers = {
    # Request headers. Replace the key below with your subscription key.
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': '9a899136784940ebadbe150dc9d28b39',
}

params = urllib.parse.urlencode({
    # Request parameters. All of them are optional.
    'visualFeatures': 'Categories',
    'details': 'Celebrities',
    'language': 'en',
})


def findMatch (link): 
    try:      
        body = "{'url':\'"+link+"\'}" 

        h1 = http.client.HTTPConnection('www.cwi.nl')
        conn = http.client.HTTPConnection('northeurope.api.cognitive.microsoft.com') 
        conn.request("POST", "/vision/v1.0/analyze?%s" % params, body, headers) #
        response = conn.getresponse() 
        data = response.read() 
        conn.close() 
        d1=json.loads(data)     
         
        if (str(data).__contains__('"celebrities":[]') or str(data).__contains__('"categories":[]')):  
            #print ("catching empties has worked")
            return("This person could not be matches by the Face API");    
        else:  
            name = (d1['categories'][0]['detail']['celebrities'][0]['name']) 
            score = (d1['categories'][0]['detail']['celebrities'][0]['confidence'])  
            percentage = (score * 100) 
            rounded_percentage = round(percentage,2) 
            classification = (d1['categories'][0]['name'])       


        if name == "":  
            #print("name is empty so failed")
            return("This person could not be matches by the Face API");  
        elif score == "":  
            #print("score is empty so failed")
            return("This person could not be matches by the Face API");  
        elif (classification == "people_" or classification == "people_portrait"):   
            #print (classification + " has passed the classification test and is therefore equal to people_ or people_portrait")
            return (str(rounded_percentage) + ": Certain that this is " + name);  
        else:  
            #print (classification + " has failed the classification test and is therefore not equal to people_ or people_portrait")
            return("This person could not be matches by the Face API");
        
    except KeyError:   
        #print("Failed because of exeption")
        return("This person could not be matches by the Face API");  
    
def getScore (link): 
    try:      
        body = "{'url':\'"+link+"\'}" 

        h1 = http.client.HTTPConnection('www.cwi.nl')
        conn = http.client.HTTPConnection('northeurope.api.cognitive.microsoft.com') 
        conn.request("POST", "/vision/v1.0/analyze?%s" % params, body, headers) #
        response = conn.getresponse() 
        data = response.read() 
        conn.close() 
        d1=json.loads(data)     
           
        score = (d1['categories'][0]['detail']['celebrities'][0]['confidence'])  
        percentage = (score * 100)   
        return percentage;      
   
    except KeyError:   
        #print("Failed because of exeption")
        return("This person could not be matches by the Face API");  
    
def mysplit(key):
        head = key.rstrip('0123456789')
        return head
    

#for p in fvpeople:
  
#    print("'" + p + "1" + "' : '',") 
#    print("'" + p + "2" + "' : '',") 
#    print("'" + p + "3" + "' : '',") 

vcorrect = 0 
vscores = [] 
vmatched = [] 

for key,value in Very_famous.items():
     
    link = value  
    text = findMatch(link) 
    name = mysplit(key)     
    if text != "This person could not be matches by the Face API":  
        print(key + " was matched as " + text)  
        vcorrect = vcorrect + 1  
        score = getScore(link)
        vscores.append(score) 
        if vmatched.__contains__(name): 
            print 
        else: 
            vmatched.append(name)
    else: 
        print(key + "was not matched my the face API")   
        
        
        
mcorrect = 0 
mscores = [] 
mmatched = [] 

for key,value in Medium_famous.items():
     
    link = value  
    text = findMatch(link) 
    name = mysplit(key)     
    if text != "This person could not be matches by the Face API":  
        print(key + " was matched as " + text)  
        mcorrect = mcorrect + 1  
        score = getScore(link)
        mscores.append(score) 
        if mmatched.__contains__(name): 
            print 
        else: 
            mmatched.append(name)
    else: 
        print(key + "was not matched my the face API")   
        
        
lcorrect = 0 
lscores = [] 
lmatched = [] 

for key,value in Low_famous.items():
     
    link = value  
    text = findMatch(link) 
    name = mysplit(key)     
    if text != "This person could not be matches by the Face API":  
        print(key + " was matched as " + text)  
        lcorrect = lcorrect + 1  
        score = getScore(link)
        lscores.append(score) 
        if lmatched.__contains__(name): 
            print 
        else: 
            lmatched.append(name)
    else: 
        print(key + "was not matched my the face API")         
        
        
        
        
        
        

        
print("the very famous category matched " + str(vcorrect) + " out of " + str(len(Very_famous)) + " Pictures with an average confidence rating of " + str(average(vscores)))  
str(len(vmatched))
print("a total of " + str(len(vmatched)) + " People were matched out of " + str(len(Very_famous)/3)) 

print("the medium famous category matched " + str(mcorrect) + " out of " + str(len(Medium_famous)) + " Pictures with an average confidence rating of " + str(average(mscores)))  

print("a total of " + str(len(mmatched)) + " People were matched out of " + str(len(Medium_famous)/3)) 

print("the low famous category matched " + str(lcorrect) + " out of " + str(len(Low_famous)) + " Pictures with an average confidence rating of " + str(average(lscores)))  

print("a total of " + str(len(lmatched)) + " People were matched out of " + str(len(Low_famous)/3))
            

