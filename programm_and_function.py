# -*- coding: utf-8 -*-
"""
Created on Thu Nov 17 14:00:19 2022

@author: Patrick Ablinger
"""
import time
import sys
import platform
import copy


picture = "NNNNNNNNNNNXK0OOkO0000OkkkO0KNNNNNNNNNNNфNNNNNNNNX0kdooodxkkollc:::cccox0XNNNNNNNфNNNNNNKkdodolloooo:;;;;;;;:;;;;coOXNNNNNфNNNNKkdllooc:::;;:;;,;;;;;;;;;:cclx0NNNNфNNN0dllcccc:::;;;:::;::;;::;::clllodkXNNфNXklccclol:::;;;;;:cc:;;;:;;;:ccooddokXNфNOlcccd0Oo:;;;;;;cc;,,,,;;;;:clllodoookXфKoccccdkdc;;;;,,:llcccc;,,,;;cdxdolllloOфOlcccccc:;;;;,;codxxxxdollodooodxxdo:;:dфklc::::::;;;;cdkxxxdddddxxxkkxoldkOo;,;lфxcc::::;;;;;;okkxxxddddxxxxkOOxoldo:,,,cфk:;::;;;;,,,;clllooddddxxxddxdolldo:,,,oфKo;;:;;,,,,,,,;:::cccclcc::::cclooc;,,:OфN0c;:::;,,''''',,,,,,,;:;;;;:ccll:,,,;xNфNN0l:::;'''''''',,',,,,:cc:ccccl:,,,;xXNфNNN0d:,'''''''',,,,,,,,;ccllcccc:;;ckNNNфNNNNXkc,''''',,,,,,,,,,codddol:;;cdKNNNNфNNNNNNXkl;''',,,,,,,,,,:dkxoc;:lxKNNNNNNфNNNNNNNNNKkdl:;,,,,,,,,;cllldk0XNNNNNNNNфNNNNNNNNNNNWX0kdoccccclodk0XNWNNNNNNNNNNλNNNNNNNNNNNXK000KKK0OkxxxkkOKNNNNNNNNNNNфNNNNNNNNXOkxxxkkdolc::clc:;;cok0XNNNNNNNфNNNNNNKOxlloodoc::::::::;;;;;::ldOXNNNNNфNNNNKkoolccc::c::::::::;;;:ccclllodOXNNNфNNXOollcc::::ccccc:ccc:::cclollloollxKNNфNXxlcccllc:::cllccc::::;:ccclooooololdKNфNkccccd0Ol::llc;;::::;;::clccoooolool:dXф0occccdkoc:codool:;,;;;;:oddolcllllll:;kфkccccccc::lxO000kdlloooollodxdooc,,:c:,lфxcccc:::cx0000Okxxddddxxxocldkkd:,,,;:,cфxc::::::o0K00Okxxxddddxkxxoclol:,,,,,,,cфkc:::;;;cdddxxdddddddodddolclooc,,,,,,,oфKo:;;;;;,;:ccccccc:::::::cclooc;,,,,,,:OфNOl:;,,,,,,,,,,,;;;;;;;;::cll:,,,,,,,;dXфNNOl;,,,,'''''''';::::::::cc:,,,,,,,;dXNфNNN0l,''''''''',,,;ccccccccc:;:;,,,:kXNNфNNNNXx:'''''',,,,,:looooool:,::;,:d0NNNNфNNNNNNXkl;'',,,,,,,cldxxdl:;,,;lx0NNNNNNфNNNNNNNNN0xoc:;,,,,,,:cc:::cox0XNNNNNNNNфNNNNNNNNNNNNX0kdlccclllldk0KNWNNNNNNNNNNλфNNNNNNNNNNNXKKKKKK0kddddxxk0KNNNNNNNNNNNфNNNNNNNNX0OOkxdollloooc:;;:cldk0XNNNNNNNфNNNNNNKkdoddlccccccc:::;:::cccllokXNNNNNфNNNNKxlccccccccccc:::::cllllllooc:lkXNNNфNNXOocccclollllllcclllloooooloolcc::dKNNфNXklcccloooollllccclolclooooolllllc:;lKNфNkccccd0Kklccccccccloolclolollllll:;::oKф0occccx0KOxdl:::::cdxxdolcccccllcl:,;;:xфkcccclx0KXXKOxxkxdolloddolol;,,;:l:,,,;oфxccclkXXXX000OOOkkdlc:coxxdc,''',::,,,;lфxcccoKXXXK000Okxxxxdol:cll:,,,,,,,,,,,,cфkc::lxkkOOkkkxdoooollccclol;,,,,,,,,,,,oфKo;;;:clllllcc:;;::::cclol:,,,,,,,,,,,:OфNOc;;,;;;,,,;;;,;;;:::clc,,,,,,,,,,,,;dXфNNO:,,,,,''',;::::::::cc;,,,,,,,,,,,;dXNфNNNOl,''''''',;::cc::ccc:;::;,,,,,,:kXNNфNNNNXx:''''',,;cloooollc;;::,,,,,:d0NNNNфNNNNNNKkl;,',,,;coxxdol:;,,,,,;cx0NNNNNNфNNNNNNNNN0xoc:;,,;cc::;;;;:cox0XNNNNNNNNфNNNNNNNNNNNNX0kdlclclllldk0XNWNNNNNNNNNNλфNNNNNNNNNNNNXXKKK0xddddddxkOKXNNNNNNNNNNфNNNNNNNNXKOkdoooddlcc:;;:c:ccldOXNNNNNNNфNNNNNN0kxdlcllllcc::cc::cccool;;cxKNNNNNфNNNN0dlccccllllcccloooooooooolc;;,ckXNNNфNNXOlcloooooolloddxxxdddoooolcc::;,,oKNNфNXxlccdkkxoollodooxxxxddoolllll::;;,,lKNфNkccoxOXKxoooodxdodddooolllccl:;;::;,,oKф0oclx0XXklcccokOkxollccc:ccccc;,,;;:,,;xфkclkKNNX0O0Okxxxkkdlllc;',,;:c;''',;;;;lфxlOXNNXXXKKKKOdcldxxdo:,'''',::,,,,;::;cфxo0NNXXXX0000Oxl:clcc;,'''''',,,,,,,,;,cфkldO00000Okxxdlc:ccloc,'''',',,,,,,,,,;dфKo:loooool:::::::cllc;'''',,,,,,,,,,,,c0фNOc;:;;;:;;;;;;::c:,'''',,,,,,,,,,,,,;xXфNNk:,,,,,;:::::::::,'',,,,,,,,,,,,,,;dXNфNNNOl,','',::::::::;,,;:,,,,,,,,,,,:kXNNфNNNNXx:,'',;clllllc;,,;:,,,,,,,,,:dKNNNNфNNNNNNKkl;'';coddoc;,,,,,,,,,,;lxKNNNNNNфNNNNNNNNN0xoc:;:c:;,,,,,,;:lox0XNNNNNNNNфNNNNNNNNNNNNX0kdlllllllldk0XNNNNNNNNNNNNλфNNNNNNNNNNNNXKKKOxddoddddxkOKNNNNNNNNNNNфNNNNNNNNX0kxddxdlc:::clccc:;:cdOXNNNNNNNфNNNNNN0kollllllcllcclllloolc;,',cxKNNNNNфNNNNKxllloollldxxxxxxddddolc::;,''ckXNNNфNNXOdooddodxxkOOkkxxxxdoollc:;;,''',oKNNфNXxoddxkkxxkxk0OOkxxxdollllc:;;,'''',lKNфNkooodOXXOkOxxOkkxoooolllc;;;:::,,',,,lKф0dkOddO0kOKK0xdoolclllccc:,',,;;;,,,,';kфOOXNK0KK0OOK0kxxl;',,,;:c;'''',;;,,;;,,lфKXNNNXNNXkdxO0Oxc,''''',;;,''',,;::;;,;lфKXNXNXXXX0xlodl:,''''''''''''',,,,;;,,:xфKO0KKKOOkxollloc,''''''''''''',,,,,,,:lkфKxdddoccccccllc;''''''''',,,,,,,,,,,;co0фNOc:::;;;:::cc,''''''''',,,,,,,,,,,,,:xXфNNk:,;:::::;::,'',,''',,,,,,,,,,,,,,;dXNфNNNOl,,;:::::::;,;;,,,,,,,,,,,,,,,,:kXNNфNNNNXx:,;:cllcc;,;:,,,,,,,,,,,,,,:d0NNNNфNNNNNNXkl;:cooo:,,,,,,,,,,,,,,;lxKNNNNNNфNNNNNNNNN0kollc;,,,,,,,,;;:cok0XNNNNNNNNфNNNNNNNNNNNNX0kdolclcclldk0XNNNNNNNNNNNNλфNNNNNNNNNNNXXX0kxddxxdooddxOKNNNNNNNNNNNфNNNNNNNNKOkxxdoccclooolc:,,,;cdOXNNNNNNNфNNNNNN0kdlloooolodddxxdoc;,,,'',cxXNNNNNфNNNNKxoooooxkkkOkkkkxxdl:::,''''''ckXNNNфNNN0xddxkO0000OOOkxdddoc:::;,'''''',oKNNфNXOxddk00KKKK0OOkdddoolc:;;,'''''''''lKNфNOddxk0NXKK00kxxddoolc;;:::;,''',,''',lKфXOoodONNKOkxdoddollc;,'',,;;,'',,,,,,,;xфNXKK00KXKOOd:,;;:cc;'''''',;;,,;;,,,,,,lфNNNNN0xOKXOl;,,,',;;,,'''',,;:;;;,,,;::lфNNNNNKkdxxl;,,,'''''''''''''',,,,,,;coodфXKK00kddodo;'''''''''''''''',,,,,,;coddkфXOdlclloodc,''''''''''''''',,,,,,,collo0фNOl:::cclc,''''''''''''''',,,,,,,,;:;;xNфNNkc:c::::,'''''''''''',,,,,,,,,,,,,;dXNфNNNOl::::::;';;,'',,,,,,,,,,,,,,,,,:kXNNфNNNNXklcclc:,,;,,,,,,,,,,,,,,,,,;:dKNNNNфNNNNNNKkdlll:,,,,,,,,,,,,,,,,;:oxKNNNNNNфNNNNNNNNN0kxo:;;,,,,,,,,;;cldOKNNNNNNNNNфNNNNNNNNNNWNX0kdolcclllldkKXNNNNNNNNNNNNλфNNNNNNNNNNNNX0OkxxxoooooodxOKNNNNNNNNNNNфNNNNNNNNX0kxolloooolcc:,,,,,;ldOXNNNNNNNфNNNNNNKkdoododxxkkxolc:,,,,'''',cxXNNNNNфNNNNKkddxkO0000OOxocccc;,'''''''''ckXNNNфNNN0xkO00KKK0OOkkdl::::;,'''''''''',oKNNфNXOkkOKXXXK0Okkxdoc:::;,'',''''''''',lKNфN0kO00XNNK0Okxxl::c:cc:;,''',''''''',,lKфKxkXXKXKOkkxddl;,,;;;;;;''',,,'',,,,,,;xфXK0XXK0x:::coo:,,'''',;;,',;,,,,,,,,,,,lфNN0OXNOl;;;,;c:,''''',,;;;;,,,,,,;:::;,cфNNKOkkl;;,,,,,,''''''''',,,,,,,,:loooc;cфXKOxxkd:,,,,,'''''''''''''',,,;:loodxo:oфXxlodxl;,,,,''''''''''''',,,,,:lllllolcOфNOlcoo:,,,'''''''''''''',,,,,,,:c:;,;:xXфNNOlcc:,''''''''''''''',,,,,,,,,,,,,;dXNфNNN0oc::,,;,''''''',,,,,,,,,,,,,,,;ckXNNфNNNNXOoc:,,,,'',,,,,,,,,,,,,,;;;;cdKNNNNфNNNNNNX0xl;,,,,,,,,,,,,,,;;;;:lxOKNNNNNNфNNNNNNNNNKOdc:;,,,,,,,,,;cldOKXNNNNNNNNNфNNNNNNNNNNNNX0kdlllccllox0XNNNNNNNNNNNNNλфNNNNNNNNNNNXK0OkkxdollllodkOKNNNNNNNNNNNфNNNNNNNNX0kdodddolc;,;;,,,,,:ldOXNNNNNNNфNNNNNNKkxddxkOOkdl:;;;,,,,'','',cxKNNNNNфNNNNKOkO0K000Oxool:;,,,,''''''''''ckXNNNфNNNK00KKKK00Oxoccc:;,,,,''''''''''',oKNNфNNK0XXXNXK0Oxdlcc:;,,,,,'''''''''''',lKNфNX0KXKXNNKkllllll:,,','',''''''''',,,,oKфXKK0OOKX0kl;;::c:;,'',,,''''',,,,,,,,,;xфXXXOocldxo;;;,,;:;,',,;,,,'''',,,,,,,,,lфKKXkc:;:ll:;,,,,;;;;,,,,'',,,;::::;,,,,cфXOkl:;;;;;;,,,'''',,,,,,''',clloolc;;,,cфKkko;;;;,,,,''''''''''''',;clolodxoc;,;oфXkxo;;,,,,,'''''''''''''',clllccloo:;,:OфN0dc;,,,,,''''''''''''',,,;::;;,,;;;,;xXфNNOl;,,,''''''''''''''',,,,,,,,,,,;;:xXNфNNN0o:,,,'''''''''',,,,,,,,,,,,,;;;ckXNNфNNNNXOl;,''''''''',,,,,,,,,;;;;;;cdKNNNNфNNNNNNXOo;''',,,,,,,,,,;;;;:cdxkOKNNNNNNфNNNNNNNNNKkoc:;,,,,,,,;:cox0KNNNNNNNNNNNфNNNNNNNNNNWNX0kdlccllllx0XNNNNNNNNNNNNNNλфNNNNNNNNNNNXK0OkxdolllllodkOKNNNNNNNNNNNфNNNNNNNNXOkkxdlc::;;,,,,,,,,:ldOXNNNNNNNфNNNNNNKOkkOOkdl::;;,,,,,,,,'''',cxXNNNNNфNNNNXKKK00Oxddl:;;,,,,,,''''''''',ckXNNNфNNNXXXKKKOdlol:;;;,,,,,'''''''''''',oKNNфNNXXXXKKKkoll:;;;;,,,,''''''''''''',,lKNфNXKK0KXNKkdol:;,,,,,''''''''''''',,,,,oKфX0OOOOOOdlllc;,;;,,,''''',,,,,,',,,,,,;xфXklokdc::;:c:;;;;,,,,'''''',,,',,,,,,,,lфXd::lo:;;;;:cc:;;,'',''',;;;:;,,,,,,,;,cф0l::;:;;;,,,,,,,,''''',:clllll:;;,,,,;,cфKo:;;;;,,,,,,''''''',;:lllloddoc;,,,;;;oфXx:;;;,,,,,'''''''',;:cccccclooc;,,;;;:OфNOc,;,,,,'''''''''''',;:;;,,,;;;,,;;;:xXфNNk:,,,''''''''''''',,,,,,,,,,,;;;;;:xXNфNNN0l;,'''''''''''',,,,,,,,,;;;;;;;ckXNNфNNNNXkc,''''''''',,,,,,,;;;;;;;;;cdKNNNNфNNNNNNXkl;''',,',,,;;;;;;:ldkkdoxKNNNNNNфNNNNNNNNN0koc:;,,,,;;;:lx0KXNXXXNNNNNNNNфNNNNNNNNNNNNX0kdolllllxKXXNNNNNNNNNNNNNNλфNNNNNNNNNNNXK0OxdollllloodkOKNNNNNNNNNNNфNNNNNNNNXK0xolc::;;;;;,,,,,,:ldOXNNNNNNNфNNNNNNXK0Oxoc:::;;;,,,,,,,,,,,',cxXNNNNNфNNNNNX0Okxdl:::;;;,,,,,,,'''''''',ckXNNNфNNNXXX0doolc:;;;;,,,,,,,''''''''''',oKNNфNNNX0Oxxxoc::;;;,,,,,,''''''''''',,,,lKNфNXKOxxOX0o::::;,,,,''''''''''''',,,,,,oKфX0OdcoOOxc::;;;,,,,,,,,,''''''',,,,,,,;xфkxdc:cooc:::;;;,,,'''',,,'''''',,,,,,,,lфxloc::cllc::;,,,,,,;:;;;;,,,,,,,,,,,,,,cфx:::;;;;;;;;,,,',:ccccccc:;;,,,,,,,,,;,cфk:;;;;;;,,,,,',;:ccccclooll:,,,,,;;;;;;oфKl;;;,,,,,,''',:c::c:::clol:,,,,;;;;;,:OфNO:,,,,,,'''''',;;;;,,',,;;;,,,;;;;;;:xXфNNk:,,,'''''''''',,,,,,,,,,,;;;;;;;;:xXNфNNN0l,''''''''''',,,,,,,,,;;;;;;;;;ckXNNфNNNNXx:'''''''',,,,,,,;;;;;;;;;;;cdKNNNNфNNNNNNKkl;''',,,,;;;;;:coxOkdcclxKNNNNNNфNNNNNNNNN0koc:;,,;;::lkKXXXK0KKXNNNNNNNNфNNNNNNNNNNWNX0kdolloxOKXNXXXNNNNNNNNNNNNλфNNNNNNNNNNNXKOkxdollllloodkOKNNNNNNNNNNNфNNNNNNNNXKkolc:::;;;;;,,,,,,:ldOXNNNNNNNфNNNNNNXKkoc::::;;;;;;,,,,,,,,'',cxXNNNNNфNNNNX0Oxlc:::;;;;;;,,,,,,,,,,'''',ckXNNNфNNNX0dolcc::;;;;;;,,,,,,''''''''''',oKNNфNNKkxolodl::;;;;,,,,,,,'''''''''''',,lKNфNKkxxoxK0d:;;;;,,,,,,,''''''''',,,,,,,oKфXxlddlxOdc:;;;;;,,,,''''''''',,,,,,,,,;xфOlcolcllc:;;;,,,,,,''''''''',,,,,,,,,,,lфkcclolcc:;;;;:c:;:;,,'''''',,,,,,,,,,;,cфx:::::::;;,;llllcc::;;,,',,,,,,,,,,,,;,cфk:;;;;;;,,;clllcclllcc:,,,,,,,,,,,,,;;;oфKl;;;,,,,,:lc:::::clll:,,,,,,;;;;;;;;,:OфNO:,,,,,,,,,;;,,'',,;;,,,,,,;;;;;;;;;;xXфNNk:,,,''''''''''''',,,,,,,;;;;;;;;;:dXNфNNNOl,''''''''''',,,,,,;;;;;;;;;;;;ckXNNфNNNNXx:'''''',,,,,,;;;;;;;;;;;;;;cdKNNNNфNNNNNNXkl;'',,,,;;;ccoxkOkl::::lxKNNNNNNфNNNNNNNNN0xoc:;;;;oO0KXNXOxO0O0XNNNNNNNNфNNNNNNNNNNNNX0kdoox00KXXX00XNNNNNNNNNNNNλфNNNNNNNNNNNX0OkxdollllloodkOKNNNNNNNNNNNфNNNNNNNNXOxoc::::;;;;;;,,,,,:ldOXNNNNNNNфNNNNNNKkoc::::::;;;;;;,,,,,,,,',cxXNNNNNфNNNNXOocc::::::;;;;;,,,,,,,,''''''ckXNNNфNNN0dlccc::::;;;;;,,,,,,,,,'''''''',oKNNфNXOollclol:;;;;;;,,,,,,,,,'''''''''',lKNфN0dlclx00o:;;;;;,,,,,,'''''''''',,,,,,oKфKxolclxOdc:;;;;,,,,,,''''''''',,,,,,,,;xфkolllccc:;;;;;,,,,,'''''',,,,,,,,,,,,,,lфxoolc:::clccc:;,,'''''''',,,,,,,,,,,,,,cфd:cc:::ldddool:;,''''''',,,,,,,,,,,,,;,cфk:;;;;codooodolc;,''''',,,,,,,,,,,,,;;;oфKl;;;;collc:cccc;''''',,,,,,,,,,;;;;;,:OфNO:,,,,;::,'',,,,,',,,,,,;;;;;;;;;;;;;xXфNNk:,,,,,'''''''',,,,,,,;;;;;;;;;;;;;dXNфNNNOl,''''''''',,,,,,,;;;;;;;;;;;;;ckXNNфNNNNXx:'''',,,,,,,;;;;;;;;;;;;;;;:dKNNNNфNNNNNNKkl;,,,,,;:oxkkkxl:cc:;;:lxKNNNNNNфNNNNNNNNN0kol:;:d0KXXXKOdxkxdk0XNNNNNNNNфNNNNNNNNNNNNX0kdxk0KXXX0kk0XNNNNNNNNNNNNλфNNNNNNNNNNNX0OkxdollllloodkOKNNNNNNNNNNNфNNNNNNNNKOdlc:::::;;;;,,,,,,:ldOXNNNNNNNфNNNNNN0xl::c:::::;;;;;,,,,,,,,',cxXNNNNNфNNNNKxc::::::::;;;;;;,,,,,,,''''''ckXNNNфNNNOlcccc:::::;;;;;,,,,,,,''''''''',oKNNфNXklccclol::;;;;;;,,,,,,,''''''''''',lKNфNklcccxK0o::;;;;;,,,,,,,'''''''',,,,,,oKф0occclxOdc:;;;;,,,,,,,''''''',,,,,,,,,;xфOllc:ccc:;;;;,,,,,,,,,''''',,,,,,,,,,,,lфklcccolll:;;;,,,,,'''''''',,,,,,,,,,,,,cфxc:cdxxxdl:;,,,,''''''''',,,,,,,,,,,,;,cфk::oxxdxkdoc,,,''',,,,,,,,,,,,,,,,,,;;;oфKl;loolllooc,''''',,,,,,,,,,,,,,,,;;;,:OфNO:;:c;,,,,,''''',,,,,,,,,,;;;;;;;;;,;xXфNNk:,,,,'''''',,,,,,,,,,;;;;;;;;;;;;;dXNфNNNOl,''''''',,,,,,,,;;;;;;;;;;;;;,ckXNNфNNNNXx:'',,,,,,,;;,;;;;;;;;;;;;;;cdKNNNNфNNNNNNKkl;,,,;lxkkxl:::c:;;;;;:lkKNNNNNNфNNNNNNNNN0kdllx0KKK0kkxxdolodk0XNNNNNNNNфNNNNNNNNNNWNX0OO00KKXKkdxO0XNWNNNNNNNNNNλфNNNNNNNNNNNX0OkxdollllloodkOKNNNNNNNNNNNфNNNNNNNNKOdoc::::;;;;;,,,,,,;ld0XNNNNNNNфNNNNNN0xlccc:::::;;;;;,,,,,,,'';lkXNNNNNфNNNN0dlcccc::::;;;;;,,,,,,,,''''',lOXNNNфNNXOlcccccc::::;;;;,,,,,,'''''''''';dKNNфNXklcccoolc:::;;;;,,,,,,'''''''''''',lKNфNklcclxK0o:::;;;;,,,,,,'''''''''''',,,oKф0occclxkdc:;;;;,,,,,,,'''''''',,,,,,,,;xфkccccccc::;;;;;,,,,''''''''',,,,,,,,,,,lфxloooc::;;;;;,,,,,''''''',,,,,,,,,,,,,,cфxokkxoc:;;;,,,,,''''''',,,,,,,,,,,,,,;,lфkdxkOkdc;;,,,,,''''''',,,,,,,,,,,,,,;,;oфKxoooddc;,,,,,,,'''',,,,,,,,,,,,,,;;;,:OфNOl:;;;;,,,',,,,,,,,,,,,,,,,,,,,;;;;,;xNфNNk:,,,,,,,',,,,,,,,,,,,;;;;;;,;;;;,:xXNфNNNOl,''',,,,,,,,,,,,;;;;;;;;;;;,,;lONNNфNNNNXx:,,,,,,,,,,,;;;;;;;;;;;;;;;cxKNNNNфNNNNNNXkl;,:dxxdc;::c:;;;;;;;;:okKNNNNNNфNNNNNNNNN0kxO0KK0kkkkxolcccldk0XNNNNNNNNфNNNNNNNNNNNNXKKKKKK0Oxooxk0XNNNNNNNNNNNNλфNNNNNNNNNNNX0OkxdollllllodkOKNNNNNNNNNNNфNNNNNNNNKOdoc:::;;;;;;,,,,,,:ok0XNNNNNNNфNNNNNN0xlcccc:::;;;;;;,,,,,,,,:cokXNNNNNфNNNN0dlccccc::::;;;;,,,,,,'''',;;:oOXNNNфNNXOlccccccc::;;;;;,,,,,,'''''''',;:oKNNфNXklcclodlc::;;;;;,,,,,''''''''''',,,lKNфNklcclxK0dc:;;;;;,,,,,,''''''''''',,,,oKф0occclxOdc:;;;;,,,,,,,'''''''''',,,,,,;xфklcccccc::;;;;,,,,,'''''''''',,,,,,,,,,lфkolcc::::;;;;,,,,,'''''''',,,,,,,,,,,,;lф0kdl:::;;;;;,,,,''''''',,,,,,,,,,,,,,;;lфKOOdc;;;;;;,,,'''''''',,,,,,,,,,,,,,,;;oфXkddc;;,;;,,,'''',,,,,,,,,,,,,,,,,;,;;cOфNOc;;;,,,,,,,'',,,,,,,,,,,,,,,,,,;;,;cxXфNNk:,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,;:lkXNфNNNOl,,,,,,,,,,,,,,,;;;;;,,,,,,,;:coOXNNфNNNNXxc,,,,,,,,,,;;;;;;;;,,,;;::cokKNNNNфNNNNNNXklcoxdl:;::;;;;;;;;;;::coxKNNNNNNфNNNNNNNNNK0KK0Okkkdoccc:;::ldk0XNNNNNNNNфNNNNNNNNNNNNNXXXK0Odoooodk0XNWNNNNNNNNNNλфNNNNNNNNNNNX0OkxdollllloodkOKNNNNNNNNNNNфNNNNNNNNKOxoc::::;;;;;,,,,,:ldx0XNNNNNNNфNNNNNN0xocccc:::;;;;;;,,,,,;cccclkXNNNNNфNNNNKxlccccc::::;;;;;,,,,,',;::::;lOXNNNфNNXOoclcccc::::;;;;,,,,,''''',,;:;,;oKNNфNXklcclodoc:::;;;;,,,,,'''''''',;,,,,lKNфNklcclkK0d::::;;;,,,,,'''''''''',,,,,,oKф0occcokOdc:;;;;;,,,,,,'''''''''',,,,,,;xфkccccllc::;;;;;,,,,'''''''''',,,,,,,,;,lфxccccc::;;;;;,,,,,'''''''',,,,,,,,,,;:;lфOlc:::::;;;;,,,,,'''''',,,,,,,,,,,;;;;;lфKd:::::;;;,,,,,''''''',,,,,,,,,,,,;;;,,oфXx:;::;;;,,,,,''''''',,,,,,,,,,,,,::;,:OфNOc;;;;;,,,,,,,'',,,,,,,,,,,,,,,,;cc::xXфNNk:,;;,,,,,,,,,,,,,,,,,,,,,,,,,;clccxXNфNNNOl;,,,,,,,,,,,,,,,,,,,,,,,;;clc:lOXNNфNNNNXxc,,,,,,,,,,,;;,,,,,;;::clcccdKNNNNфNNNNNNKkxdoc;;:;;;;;;,;;;:cc:;:lx0NNNNNNфNNNNNNNNNXXKOkkxdlcc::;;;::lok0XNNNNNNNNфNNNNNNNNNNNNNNXK0kdlollldk0XNNNNNNNNNNNNλфNNNNNNNNNNNX0OkxoolllllodxkOKNNNNNNNNNNNфNNNNNNNNKOxoc::::;;;;;,,;::ccoxOXNNNNNNNфNNNNNN0xocccc::::;;;;,,,:lllc:;;lkXNNNNNфNNNNKxlcccccc:::;;;,,,,,,:::cc:;,;lkXNNNфNNXOollccccc:::;;;,,,,,,,,,;:;,,,,,,oKNNфNXkllllodlc:::;;;,,,,,,'''',;,'',,,''lKNфNkllllxK0dc::;;;,,,,,,''''''',,,,,,,',lKф0ollllxOdc::;;;,,,,,'''''''''',,,,,,,,;xфklllccccc::;;;,,,,,'''''''''''',,,;,,,,lфxcccc:::::;;;,,,,,'''''''''',,,,;;;;;;,cфxccc:::;;;;;,,,,'''''''',,,,,,,;;;;;;;,cфkc::::;;;;,,,,,'''',,,,,,,,,,,,;;,,,;;;oфKo::;;;;;,,,,''''',,,,,,,,,,,,;:;,;,;;:OфNOc;;;;;;,,,'''''',,,,,,,,,,,,;cc:;;;cxXфNNkc;;;,,,,,,,,,,,,,,,,,,,,,;:llccc:cxXNфNNN0l;,,,,,,,,,,,,,,,,,,,,;:cllc:::ckXNNфNNNNXxc,,,,,,,,,,,,,,,,;::cllc::;:dKNNNNфNNNNNNXOxl;;;;;,,,,;;;:cc::;;;;lxKNNNNNNфNNNNNNNNNX0OOxdlc::;;;;;;;:cox0XNNNNNNNNфNNNNNNNNNNNNNXK0kolllllldk0XNNNNNNNNNNNNλфNNNNNNNNNNNX0Okxdolllloodxk0KNNNNNNNNNNNфNNNNNNNNKOxoc:::::;;;::cc:::clx0XNNNNNNNфNNNNNN0xocccc::::;;:clolllc:;,,:lkXNNNNNфNNNNKxlcccccc:::;;;;:cccccc;;;;;;;ckXNNNфNNXOolccccc::::;;;,,,;;:::;,,,,,,'',oKNNфNXklllloolc:::;;;,,,,,,;;,''',,''''',lKNфNkllllx0Ooc::;;;,,,,,,''',,,'',,''',,,lKф0oclllxkdc::;;;,,,,'''''''',,',,,,,,,,;xфklcccccc::;;;;,,,,,''''''''',,,,,,,,,,,lфxccccc:::;;;;,,,,,''''''''',;;;;;;,,,,,cфxccc::::;;;,,,,,''''''''',;;;;;;;;;,,,,cфkc::::;;;;,,,,,''''''''',,;;,,;,,;;;,,,oфKo:::;;;,,,,,,''''',,,,,,,;:;,,,,,;;;,:OфNOc;;;;;,,,''''''',,,,,,,,:cc:;;;;:::;xXфNNkc;;;,,,,''''',,,,,,,,,:llccccc::;:dXNфNNN0l;,,,,,,'',',,,,,,,;cllcc::::;;:kXNNфNNNNXkc,,,,,,,,,,,,;::cllcc::;;,,:dKNNNNфNNNNNNXkl:;;,,,,,;:cc::;;;;;,,;lxKNNNNNNфNNNNNNNNNK0Oxolc:;;;;;;;;;:cox0XNNNNNNNNфNNNNNNNNNNNNNX0kdllllllldk0XNNNNNNNNNNNNλфNNNNNNNNNNNX0OkxdolooooodxO0KNNNNNNNNNNNфNNNNNNNNKOxoc:::::cllll:;;;;cox0XNNNNNNNфNNNNNN0xocccc:::ldddddoc:;;;;;;:lkKNNNNNфNNNNKxlccccc::::loloool:;;;;;;;,,,ckXNNNфNNXOocccccc:::;;:cccc:;;,;;,,'''''',oKNNфNXklccloolc:::;;;;:;;,,,',,''''''''''lKNфNklcclxKOo::;;;;,,,,;;,,',,'''''''',',oKф0occclxkdc:;;;;,,,,,,,,,''',,'''',,,,';kфklcccccc:::;;;,,,,'''''',,,,',',,,,,,,,oфxccccc:::;;;;,,,,'''''',;;;;;,,,,,,,,,;xфxccc:::;;;;,,,,,''''',;;,;;;;;,,,,,,,,:kфkc::::;;;;,,,,,'''''';;,,,,,,,;;,,,,,,:kфKo::;;;;,,,,,,''''''';:;,,,,,,;;;,,,,,c0фNOc;;;;,,,,,'''''','',cc:;;;;;;:c:,,,;xNфNNkc;;,,,,''''''',,,;:lccc:::c:::;,,;dXNфNNN0l;,,,'''''',,,;cllcc::::c:;;,,,ckXNNфNNNNXkc,,,,'',,,;:ccccc::;;,;,,,,:dKNNNNфNNNNNNXkl:;,,,;:c:;;;;;;;;;,,,;lxKNNNNNNфNNNNNNNNNKOxdl:;;;;;;;;,;;:cox0XNNNNNNNNфNNNNNNNNNNNNNKOxollllllldk0XNNNNNNNNNNNNλфNNNNNNNNNNNX0OkxdooollodxkO0XNNNNNNNNNNNфNNNNNNNNKOxocccllollc:;;;;;cldO0XNNNNNNNфNNNNNN0xoccccdxxxxolc:;;;;;::;::cxXNNNNNфNNNNKxlccccclddddol::::;;;;;;;,'',ckXNNNфNNXOlccccc:cclolc::;:;;,,,,'''''''',oKNNфNXxlcccoolc::cc:;;,;;;,''''''''''''',oKNфNklcccd0Oo:::;::;;,,,,,''''''''''''',;dXф0occclxkdc:;;;;;;,,,,,,,''''''''''',,,l0фklcccccc::;;;,,,,,,,,,,''''''',,,,,,,;d0фxccccc::::;;;,,,,;;;;;;,,'''',,,,,,,;oO0фxccc::::;;;,,,,;;;;,;,,;;,,,,,,,,,,,:k0Kфkc::::;;;;,,,,,;;,;,,,,,,,,,,,,,,,,,:dk0фKo::;;;;,,,,,'',;;,,,,,,,,;;,,,,,,,,;cd0фNOc;;;,,,,,'''',::;;;;;;;;;;::;,,,,,;:xNфNNkc;,,,,'''''';cc:::::::::::;;,,,,,;dXNфNNN0l;,'''''',;cc:::::::::;;,,,,,,,:kXNNфNNNNXkc,'',,,:ccc:::;;,,,,,,,,,,,:dKNNNNфNNNNNNXkl;,,;::;;;;;,,,,,,,,,,;lxKNNNNNNфNNNNNNNNNKkxoc;;;;;,,,,,,;:cox0XNNNNNNNNфNNNNNNNNNNNWN0kdollcccclok0XNNNNNNNNNNNNλфNNNNNNNNNNNX0OkxddoooodxkO0KXNNNNNNNNNNNфNNNNNNNNKOxooooooc:;:::::cccdxxOXNNNNNNNфNNNNNN0xoloxkOkdlc:;::;:::;;c:,,ckXNNNNNфNNNN0xlcloxxkxolcc:::;;;;;;,''''',ckXNNNфNNXOlcccloddolcc:;;;;,,,,,,''''''',;dKNNфNXklccclddoc:::::,,,,,'''''''''''',;:oKNфNklcccd0Oocc:;;:;,,,'''''''''''''',;:;oXф0occcldkdc:::;,;;,,,'''''''''''''',;llckфklcccccc::;;;;;;,,,'''''''''''''',;lxOkOфxcccc::::;;;::;;;;,''''''',,,,,,,;dkOOO0фxccc:::;;;::;;;;;;,,,''''',,,,,,,lO0000Kфkc::::;;;;;;,,;,,,,,,,,''',,,,,,;cdxkOO0фKo::;;;;,,;:;,,,,,,,,,,,,,,,,,,,,;clood0фNOc;;;,,,,,;::;;;;,;;;;;:;,,,,,,,;;;;cxXфNNk:,,,,,'';c:::;::::::;;;,,,,,,,,,,:kXNфNNN0l,,''',:::::;;:::;;,,,,,,,,,;,;cONNNфNNNNXx:,',:cc::;;,,,,,,,,,,,,,,,;cxKNNNNфNNNNNNXkl::;,,,,,,,,,,,,,,,,,;;lkKNNNNNNфNNNNNNNNN0kdl:;;,,,,,,,,,;:cox0XNNNNNNNNфNNNNNNNNNNWNX0kdolccccclox0XNNNNNNNNNNNNλфNNNNNNNNNNNX0OkxddddddxkO0KKXNNNNNNNNNNNфNNNNNNNNKOkxdol::c::ccccclxdclx0XNNNNNNNфNNNNNN0kxkOOdol::c:clcc;;:c:,,';lkXNNNNNфNNNNKxoxkkxdlllc::::;::,,,'''''',;lOXNNNфNNXOlldddollc:::;;;,,,,,''''''',,;;:dXNNфNXxlclddolcc:;;;,,,,,,,''''''''';;;;:dKNфNkccclkK0occ;;;,,,,,,,''''''''',:;,;;:xXф0occclxOdc:::;,,,,,'''''''''''',clll:;l0фkcccccccc::;;;,,,,'''''''''''',coxOkxdxOфxcccc::ccc:::;,,''''''''''',,:okkOOOOOOOфxcc:::cc;;;;;;,,''''''''',,,,lkOO0OO0000фkc::::::,,,,,,,,'''''''',,,,;codxkkOOOkOфKo::;;::;;,,,,,,,,'''''',,,,,;cllloolco0фNOc;;;,:c:;;;,,;;;;;,,',,,,,,,;;;;::;:kNфNNk:,,,;cc:;;;;:;;;;;,,,,,,,,,,,,,:clkXNфNNNOl,';:::;;;;;;,,,,,,,,,,,,,;;,:coOXNNфNNNNXx:;:::;;,,,,,,,,,,,,,,,;;,;ldOKNNNNфNNNNNNKko:,,,,,,,,,,,,,,,,;;,;cd0XNNNNNNфNNNNNNNNNKkdl:;,,,,,,,,,,;:cokKNNNNNNNNNфNNNNNNNNNNWNX0kdlcccccclox0XNNNNNNNNNNNNλфNNNNNNNNNNNXKOkxxxxxxkO00000KNNNNNNNNNNNфNNNNNNNNXKOxoccccllllllxxo:;:ox0XNNNNNNNфNNNNNNXK0kdoccllllc:::ccc;,,,,;:lkXNNNNNфNNNNX0Okxoollccccc;;;,,,,,,,,,,,;;o0NNNNфNNNOxddoolcc:::;;;;,,,,'''',,,;;;;:lkXNNфNXkoollddl:::;;;;,,,,,'''''',;;;;:::lkXNфNkllllxKOo::;;;;,,,,''''''',;;,,;;;:loOXф0oclllxOdc:;;;;,,,''''''''';cccc:;;;cxx0фkccclllc::;;;;,,,,''''''',;ldxkkxodxxxkOфxccclllc:;;;,,,,,,'''''';ldxxkkkkkOO0xdOфxcclc::::;;,,,,,'''''',,cxkkOOkkOOO00kdxфOc:c;,;;;;;,,,'''''''',,:oodxxkkOOkkkdokфKo;::;;,,,,;,,''''''',,,,:ccllloolcclld0фNOc;cc:;;;;;;;;,'''',,,,,,;;;;;::;;:clkNфNNO:;lc::;;:;;;,'',,,,,,,,,,,,;:cccclkXNфNNN0l:c:;;;;;,''',,,,,,,,,,,,,;cllcoOXNNфNNNNXkoc;,,,'''',,,,,,,,,,,,,:ododkKNNNNфNNNNNNXOo;,,,,,,,,,,,,,,;;;,;lxkOKNNNNNNфNNNNNNNNNKkdl:;,,,,,,,,,;;:ldOKXNNNNNNNNфNNNNNNNNNNNNX0kdoccccccldk0XNNNNNNNNNNNNλфNNNNNNNNNNNX0OkkxxkOO0000OO0KNNNNNNNNNNNфNNNNNNNNX0kolclooooxkkdl:;;:cox0XNNNNNNNфNNNNNNX0xolloolcclllll:,,,;;;;;;lkXNNNNNфNNNNXOxdolllllc::;;,,,;,,,,,;;;;;cd0XNNNфNNN0xollccccc::;;,,,,,,;;;;;;;;;:clokXNNфNXklllclol:::;;;,,,,,,,,;;;;;;;;;clodkXNфNklllcd0Oo::;;;,,,,,,,,;:,,,,;;;:cloddkXф0oclllxkoc:;;;,,,,,''',:cccc;,,;;cxkdooOфklllcccc:::;;,,,,,',;;codxxxdooddddxkxcoфxloll::::;;;;,,,,,;lddddxxxxxkkkOOdokOlcфxl::c::;;;;,,,,,,,cddxxxkxxxkkkO00kooo;cфOc;;;;;;,,,,,,,'',:llloddxxxkkkxxxdodo:oфKo:;,,;;;,,,'''''',;::cccllllcc:ccloo::OфNOlc:;;;;:;,''''''',,,,;;,;::;;;:cll:;dXфNNOoc::::;;,''''',,,,,,,,,,:ccccccc;;dXNфNNN0d::;;,'''''',,,,,,,,,,,:llllcc:ckXNNфNNNNXOl,''''''',,,,,,,,,,,:odddoccxKNNNNфNNNNNNXkl;,'',,,,,,,,,,,;,cxxoloxKNNNNNNфNNNNNNNNN0koc:;,,,,,,,,,;;cdxk0XNNNNNNNNфNNNNNNNNNNNNX0kdlccccccldk0XNWNNNNNNNNNNλ"
oppyright = "▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ф▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ф▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█████▓▒█████▓▒█████▓▒█████▓▒▒▒██▓▒▒█████▓▒█▓▒▒█▓▒▒▒▒▒▒▒▒▒▒ф▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▓▒▒█▓▒█▓▒▒█▓▒▒▒█▓▒▒▒█▓▒▒█▓▒▒▒██▓▒▒█▓▒▒█▓▒█▓▒▒█▓▒▒▒▒▒▒▒▒▒▒ф▒▒▒▒▒▒▒█████████████████████▓▒▒▒▒█▓▒▒█▓▒█▓▒▒█▓▒▒▒█▓▒▒▒█▓▒▒█▓▒▒▒██▓▒▒█▓▒▒▒▒▒█▓▒█▓▒▒▒▒▒▒▒▒▒▒▒ф▒▒▒▒▒██▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██▓▒▒▒█▓▒▒█▓▒█▓▒▒█▓▒▒▒█▓▒▒▒█▓▒▒█▓▒▒▒██▓▒▒█▓▒▒▒▒▒█▓▒█▓▒▒▒▒▒▒▒▒▒▒▒ф▒▒▒▒▒██▓▒▒██████████████▓▒▒██▓▒▒▒█████▓▒█████▓▒▒▒█▓▒▒▒█████▓▒▒▒██▓▒▒█▓▒▒▒▒▒███▓▒▒▒▒▒▒▒▒▒▒▒▒ф▒▒▒▒▒██▓▒▒███▓▒▒▒▒▒▒▒▒██▓▒▒██▓▒▒▒█▓▒▒▒▒▒█▓▒▒█▓▒▒▒█▓▒▒▒███▓▒▒▒▒▒██▓▒▒█▓▒▒▒▒▒████▓▒▒▒▒▒▒▒▒▒▒▒ф▒▒▒▒▒██▓▒▒███▓▒▒▒▒▒▒▒▒██▓▒▒██▓▒▒▒█▓▒▒▒▒▒█▓▒▒█▓▒▒▒█▓▒▒▒█▓▒█▓▒▒▒▒██▓▒▒█▓▒▒█▓▒█▓▒██▓▒▒▒▒▒▒▒▒▒▒ф▒▒▒▒▒██▓▒▒███▓▒▒▒▒▒▒▒▒▒▒▒▒▒██▓▒▒▒█▓▒▒▒▒▒█▓▒▒█▓▒▒▒█▓▒▒▒█▓▒▒█▓▒▒▒██▓▒▒█████▓▒█▓▒▒█▓▒▒▒▒▒▒▒▒▒▒ф▒▒▒▒▒██▓▒▒███▓▒▒▒▒▒▒▒▒▒▒▒▒▒██▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ф▒▒▒▒▒██▓▒▒███▓▒▒▒▒▒▒▒▒▒▒▒▒▒██▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ф▒▒▒▒▒██▓▒▒███▓▒▒▒▒▒▒▒▒▒▒▒▒▒██▓▒▒▒█████▓▒█████▓▒█▓▒▒▒▒▒██▓▒▒█▓▒▒█▓▒█████▓▒█████▓▒█████▓▒▒▒▒▒ф▒▒▒▒▒██▓▒▒███▓▒▒▒▒▒▒▒▒██▓▒▒██▓▒▒▒█▓▒▒█▓▒█▓▒▒█▓▒█▓▒▒▒▒▒██▓▒▒█▓▒▒█▓▒█▓▒▒▒▒▒█▓▒▒▒▒▒█▓▒▒█▓▒▒▒▒▒ф▒▒▒▒▒██▓▒▒███▓▒▒▒▒▒▒▒▒██▓▒▒██▓▒▒▒█▓▒▒█▓▒█▓▒▒█▓▒█▓▒▒▒▒▒██▓▒▒█▓▒▒█▓▒█▓▒▒▒▒▒█▓▒▒▒▒▒█▓▒▒█▓▒▒▒▒▒ф▒▒▒▒▒██▓▒▒██████████████▓▒▒██▓▒▒▒█▓▒▒█▓▒█▓▒▒█▓▒█▓▒▒▒▒▒██▓▒▒██▓▒█▓▒█▓▒▒▒▒▒█▓▒▒▒▒▒█▓▒▒█▓▒▒▒▒▒ф▒▒▒▒▒██▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██▓▒▒▒█████▓▒████▓▒▒█▓▒▒▒▒▒██▓▒▒█▓█▓█▓▒█▓▒██▓▒████▓▒▒█████▓▒▒▒▒▒ф▒▒▒▒▒▒▒█████████████████████▓▒▒▒▒█▓▒▒█▓▒█▓▒▒█▓▒█▓▒▒▒▒▒██▓▒▒█▓▒██▓▒█▓▒▒█▓▒█▓▒▒▒▒▒███▓▒▒▒▒▒▒▒ф▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▓▒▒█▓▒█▓▒▒█▓▒█▓▒▒▒▒▒██▓▒▒█▓▒▒█▓▒█▓▒▒█▓▒█▓▒▒▒▒▒█▓▒█▓▒▒▒▒▒▒ф▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▓▒▒█▓▒█████▓▒█████▓▒██▓▒▒█▓▒▒█▓▒█████▓▒█████▓▒█▓▒▒█▓▒▒▒▒▒ф▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ф▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒"
oppyright = oppyright.split('ф')
frames = picture.split('λ')
rows = picture.split('ф')
edited_rows = []
for i in range(len(rows)): #small loop to fix inconsistency with picture string
    if i == 19: #problematic index
        edited_rows.append(rows[i][:41][:40]) #to make all list of len 40
        edited_rows.append(rows[i][41:]) #-> this one surely has len 40
    else:
        edited_rows.append(rows[i][:40])  #to make all list of len 40
rows = edited_rows
       
#global variables
KMHTOMS = True
DURATION = 3
SYSTEM_DECISION = platform.system()
if SYSTEM_DECISION == 'Windows':
    SYSTEM_TYPE = False
    
    
def printHelpText():
    """well, this one describes itself the best"""
    if KMHTOMS:
        string = '[km/h] -> [m/s]'
    else:
        string = '[km/h] -> [s/m]'
    print('==================================== \n ')
    print('Die aktuelle Umrechnung ist {}.'.format(string))
    print('Das Programm gibt immer eine Nachkommastelle mehr, als der Input aus.')
    print('[exit] Beenden Sie das Programm indem Sie "exit" eingeben.')
    print('[/help] Rufen Sie diese Hilfe Funktion auf.')
    print('[/toggle] Ändern Sie die Umrechnungsrichtung.')
    print('[/rotate] Für echte Geniesser!')
    print('[/author] Anzeigen des Herstellertags')
    print('[/m/s] Umrechnen in [m/s].')
    print('[/s/m] Umrechnen in [s/m].')
    print('\n==================================== \n ')
    
def CommandHandler(input_string):
    """basic command handler, which processes inputs """
    global KMHTOMS
    lwrd = input_string.lower()
    
    if lwrd in ['/', '/h', 'help', '/help', '/hilfe', 'hilfe', '/info']:
        
        printHelpText()
        
        return 2 #exit code 'Change Needed'
    
    if lwrd in ['/toggle', '/t']:
        if KMHTOMS:
             KMHTOMS = False
             print('Nun wird von [km/h] in [s/m] umgerechnet.')
        else:
             KMHTOMS = True
             print('Nun wird von [km/h] in [m/s] umgerechnet.')        
        return 2 #exit code 'Change Needed'
    
    if lwrd in ['/exit', 'exit', 'e', '/e', '"exit"']:
        print('Vielen Dank für das Nutzen dieses Tools.')
        print('© Patrick Ablinger, 2022')
        return 0 #0 is exit key
    
    if lwrd in ['/rotate', 'rotate', '/r', 'r']:

        rotation(DURATION)
                
        return 2
    
    if lwrd in ['m/s', '/m/s', '[/m/s]', '/[/m/s]']:
        KMHTOMS = True
        print('Nun wird von [km/h] in [m/s] umgerechnet.')
        return 2
    
    if lwrd in ['s/m', '/s/m', '[/s/m]', '/[/s/m]']:
        KMHTOMS = False
        print('Nun wird von [km/h] in [s/m] umgerechnet.')
        return 2
    
    if lwrd in ['author', '/author', '/a', 'a', 'copyright', '/copyright']:
        
        blinkAuthor(DURATION)
        
        return 2
        
    return 1 #if no keyword --> try continuing processing


def loading_function():
    """function which guarentees fast calculation """
    print("Processing Input: ##", end = ' ', flush=True)
    for i in range(6):
        time.sleep(0.13)
        print("##", end=' ', flush=True)
    print(" ")
    time.sleep(0.2)
    print("Calculation Finished!")
    time.sleep(0.2)
    return
    

def kmh2ms(input_float, round = 0):
    """
    This function converts km/h to m/s and s/m
    returns a tuple of (m/s, s/m).
    
    Note that this function itself does not check wheter your inputs are of
    correct data type.

    Parameters
    ----------
    input_float : FLOAT or INT (Number)
        input: kilometers/h which you want to calculate to m/s or s/m

    Returns
    -------
    ms : FLOAT
        result in meter/seconds.
    sm : FLOAT
        result in seconds/meter.

    """
    
    ms = input_float / 3.6
    sm = 1/ms
    return ms, sm


def prepareString(input_string):
    """
    

    Parameters
    ----------
    input_string : string of input

    Returns
    -------
    out_str : prepared string

    comma_n : int number of float values (int)
        
    """
    backup = copy.copy(input_string)
    kmh_f = input_string[::-1] #reversing the input string to easier find number of values before comma
    out_str = '' #defining empty string which is going to be filled with useble '.'
    comma_n = 0 #if there is no , or . than the value is just 0
    for i, char in enumerate(kmh_f): #finding missleading ',' in string and finding out the number of float values (for rounding afterwards)
        if char in [',','.']: #checking if floating value is reached
            comma_n = i #get the index of , or . (That's how many values are after , because of reverse iteration through string)
            if char == ',': #correction check
                char = '.' #correction step
        out_str += char #out string is always without , but whith . (good!)
    out_str = out_str[::-1]
    return out_str, comma_n #returning fast tuple
   
         
def validateString(input_string):
    """
    

    Parameters
    ----------
    input_string : adapted prepared string
       

    Returns
    -------
    out_float : validated float from input_string


    """
          
    try :
        
        out_float = float(input_string)   # try to cast to float type 

    except ValueError:

        return '41 63 68 69 6C 6C 65 73 73 65 68 6E 65' , 0#Achillessehne
        #returning error value
    number_of_N = ''
    for char in input_string:
        if char != '.':
            number_of_N += (char)
        else:
            break
    return out_float, len(number_of_N)  #returning correct value
   
     
def TransTo(float_valid, raw_str):
    """ function which calculates m/s and depending on global bool
    decides which value to return (m/s or s/m)"""
    len_raw_str = len(raw_str)
    #print(raw_str, float_valid)
    meter_sec = abs(float_valid / 3.6) #actual calculation into m/s --> abs value because speed is always abs compared to velocity
    if KMHTOMS:          
        pass
    else:
        meter_sec = 1/meter_sec #invert
    
    #new implementation to give correct output in floating value with .000 inputs
    check_float = len_raw_str + 1 - len(str(meter_sec)) #should be zero
    meter_sec = str(meter_sec)
    if check_float == 0:    
        pass
    else:
        for i in range(check_float):
            meter_sec += '0'
    #print(meter_sec)
    
    return meter_sec #returns value as str

    
def rotation(duration):
    """ function which rotates earth image defined in code above"""
    for k in range(duration): 
        for i in range(0, len(rows), 20): #every 20th line is a new frame
            for j in range(20): #print single rows of each frame
                sys.stdout.write(str(rows[i+j]) + "\n") #i+j to hit exact value
                
            sys.stdout.flush()
            time.sleep(0.1) #framerate
            if SYSTEM_TYPE:               
                for l in range(20):
                    sys.stdout.write("\033[K")  # remove line
                    sys.stdout.write("\033[1A") # up the cursor

    
def displayAuthor():
    """ function which is designed to display author signature"""
    for i in range(len(oppyright)): #in this case only one image
        sys.stdout.write(str(oppyright[i]) + "\n")       
    sys.stdout.flush()
    time.sleep(0.1)
    if SYSTEM_TYPE:                
        for i in range(len(oppyright)+1):
            sys.stdout.write("\033[K")  # remove line
            sys.stdout.write("\033[1A") # up the cursor        
        sys.stdout.flush()
        time.sleep(0.1) 
       
    
def blinkAuthor(duration):
    """help function which prints author signature many times(based on GLOBAL
    duration
    """
    for i in range(duration*10):
        displayAuthor()
        time.sleep(0.1)

    
def _18_0_exceptionCheckAndPrint(calculated_func, nOfValue_func, kmh_func, nFloat_func):
    '''DOC BADLY NEEDED'''
    if len(kmh) + 1 - len(calculated_func) == 0: #should be zero if .000 value is entered and then str has correct length for rounding error aswell
        if nOfValue == len(calculated_func[:nOfValue_func]): #could be zero but the other one is with one digit less than the input
            if '.' in calculated_func[:nOfValue_func]: #checking it here explicitly
                
                output_calc = calculated_func[:-1] #returns string with one zero less
            else:
                output_calc = calculated_func #returns exactly the string
        else:

            output_calc = calculated_func ##returns exactly the string if not
    else: #for normal float --> needs rounding of value
        output_calc = round(float(calculated_func), nFloat_func+1) #returns float --> +1 because i want to include rounding error
    print('Ihre Eingabe beträgt umgerechnet {} {}. \n'.format(output_calc, unit)) #IMPORTANT: output_calc is dynamic DTYPE (float or str)
        
    
print('Falls Sie Hilfe benötigen, geben Sie /help ein.')   
print('Beenden Sie das Programm indem sie "exit" eingeben.') 
print('Bitte geben Sie die gegebenen km/h ein: ')
while True:  
    
    kmh = input()
    continueValue = CommandHandler(kmh)
    if continueValue == 0:
        break    #exit main loop
    if continueValue == 1:
        pass #do nothing (continue value == 1)
    if continueValue == 2:
        print('Entern Sie bitte ihre neue Eingabe.')
        continue #repeat Process

   
    prepared_str, nFloat = prepareString(kmh) #prepare string and number of float values
    float_valid, nOfValue = validateString(prepared_str) #converting string or restart and return number before .
    
    if float_valid == '41 63 68 69 6C 6C 65 73 73 65 68 6E 65': #Achillessehne #Betriebsgeheimnis
        print('Entern Sie bitte ihre neue, RICHTIGE Eingabe.')
        continue #repeat Process
    print(kmh)
    print(float_valid)   
    
    calculated = TransTo(float_valid, kmh) #calculated is str-type
        
    loading_function()
    
    if KMHTOMS:
        unit = '[m/s]'
    else:
        unit = '[s/m]'
        
    _18_0_exceptionCheckAndPrint(calculated, nOfValue, kmh, nFloat)
    #print(calculated)


    # if len(kmh) + 1 - len(calculated) == 0: #should be zero if .000 value is entered and then str has correct length for rounding error aswell
    #     if nOfValue == len(calculated[:nOfValue]):
    #         if '.' in calculated[:nOfValue]:
                
    #             output_calc = calculated[:-1] #returns string with one zero less
    #         else:
    #             output_calc = calculated
    #     else:

    #         output_calc = calculated
    # else: #for normal float --> needs rounding of value
    #     output_calc = round(float(calculated), nFloat+1) #returns float --> +1 because i want to include rounding error
    # print('Ihre Eingabe beträgt umgerechnet {} {}. \n'.format(output_calc, unit)) #IMPORTANT: output_calc is dynamic DTYPE (float or str)


    


