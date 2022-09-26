#!/home/ufk/ufk_venv/bin/python
import django
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "monitoring_project.settings")
django.setup()

from datetime import datetime, timezone
import pytz
localtime = pytz.timezone("Asia/Krasnoyarsk")

from monitoring.models import UK, PIF
from django.db.models import Q

import time

#solid = UK.objects.filter(uk_ogrn = '1027700227180').first()
#pifset = PIF.objects.filter(Q(pif_uk = solid) & ~Q(pif_checkpage=''))
#openam = UK.objects.filter(uk_ogrn = '1027739072613').first()
#pifset = PIF.objects.filter(Q(pif_uk = openam) & ~Q(pif_checkpage=''))
#tfg = UK.objects.filter(uk_ogrn = '1037739614604').first()
#pifset = PIF.objects.filter(Q(pif_uk = tfg) & ~Q(pif_checkpage=''))
#pragma = UK.objects.filter(uk_ogrn = '1067746469658').first()
#pifset = PIF.objects.filter(Q(pif_uk = pragma) & ~Q(pif_checkpage=''))
#veles = UK.objects.filter(uk_ogrn = '5067746107391').first()
#pifset = PIF.objects.filter(Q(pif_uk = veles) & ~Q(pif_checkpage=''))
#rwminvest = UK.objects.filter(uk_ogrn = '1057749282810').first()
#pifset = PIF.objects.filter(Q(pif_uk = rwminvest) & ~Q(pif_checkpage=''))
#gamma = UK.objects.filter(uk_ogrn = '1175476116420').first()
#pifset = PIF.objects.filter(Q(pif_uk = gamma) & ~Q(pif_checkpage=''))
#rbcapital = UK.objects.filter(uk_ogrn = '1207700192590').first()
#pifset = PIF.objects.filter(Q(pif_uk = rbcapital) & ~Q(pif_checkpage=''))
#april = UK.objects.filter(uk_ogrn = '1027700266813').first()
#pifset = PIF.objects.filter(Q(pif_uk = april) & ~Q(pif_checkpage=''))
#navigator = UK.objects.filter(uk_ogrn = '1027725006638').first()
#pifset = PIF.objects.filter(Q(pif_uk = navigator) & ~Q(pif_checkpage=''))
#arsagera = UK.objects.filter(uk_ogrn = '1047855067633').first()
#pifset = PIF.objects.filter(Q(pif_uk = arsagera) & ~Q(pif_checkpage=''))
#ew_mc = UK.objects.filter(uk_ogrn = '1056405422875').first()
#pifset = PIF.objects.filter(Q(pif_uk = ew_mc) & ~Q(pif_checkpage=''))
#ucnu = UK.objects.filter(uk_ogrn = '1077759414281').first()
#pifset = PIF.objects.filter(Q(pif_uk = ucnu) & ~Q(pif_checkpage=''))
#kspcapital = UK.objects.filter(uk_ogrn = '1077759966756').first()
#pifset = PIF.objects.filter(Q(pif_uk = kspcapital) & ~Q(pif_checkpage=''))
#aricapital = UK.objects.filter(uk_ogrn = '1127747149155').first()
#pifset = PIF.objects.filter(Q(pif_uk = aricapital) & ~Q(pif_checkpage=''))
#recordcap = UK.objects.filter(uk_ogrn = '1137746080768').first()
#pifset = PIF.objects.filter(Q(pif_uk = recordcap) & ~Q(pif_checkpage=''))
#savingsim = UK.objects.filter(uk_ogrn = '1027722009941').first()
#pifset = PIF.objects.filter(Q(pif_uk = savingsim) & ~Q(pif_checkpage=''))
#fdu = UK.objects.filter(uk_ogrn = '1037739042285').first()
#pifset = PIF.objects.filter(Q(pif_uk = fdu) & ~Q(pif_checkpage=''))
#olma = UK.objects.filter(uk_ogrn = '1037739831326').first()
#pifset = PIF.objects.filter(Q(pif_uk = olma) & ~Q(pif_checkpage=''))
#trinfico = UK.objects.filter(uk_ogrn = '1047796947857').first()
#pifset = PIF.objects.filter(Q(pif_uk = trinfico) & ~Q(pif_checkpage=''))
#ural = UK.objects.filter(uk_ogrn = '1086671002582').first()
#pifset = PIF.objects.filter(Q(pif_uk = ural) & ~Q(pif_checkpage=''))
#oreol = UK.objects.filter(uk_ogrn = '1107746237147').first()
#pifset = PIF.objects.filter(Q(pif_uk = oreol) & ~Q(pif_checkpage=''))
#redbridge = UK.objects.filter(uk_ogrn = '1167847368325').first()
#pifset = PIF.objects.filter(Q(pif_uk = redbridge) & ~Q(pif_checkpage=''))
#leader = UK.objects.filter(uk_ogrn = '1025002040250').first()
#pifset = PIF.objects.filter(Q(pif_uk = leader) & ~Q(pif_checkpage=''))
#zaouk = UK.objects.filter(uk_ogrn = '1026602948404').first()
#pifset = PIF.objects.filter(Q(pif_uk = zaouk) & ~Q(pif_checkpage=''))
#contrada = UK.objects.filter(uk_ogrn = '1047796009128').first()
#pifset = PIF.objects.filter(Q(pif_uk = contrada) & ~Q(pif_checkpage=''))
#veles_m = UK.objects.filter(uk_ogrn = '1047796515470').first()
#pifset = PIF.objects.filter(Q(pif_uk = veles_m) & ~Q(pif_checkpage=''))
#tetis = UK.objects.filter(uk_ogrn = '1107746374262').first()
#pifset = PIF.objects.filter(Q(pif_uk = tetis) & ~Q(pif_checkpage=''))
#victory = UK.objects.filter(uk_ogrn = '1067746540201').first()
#pifset = PIF.objects.filter(Q(pif_uk = victory) & ~Q(pif_checkpage=''))
#capital_am = UK.objects.filter(uk_ogrn = '1087746129888').first()
#pifset = PIF.objects.filter(Q(pif_uk = capital_am) & ~Q(pif_checkpage=''))
megainv = UK.objects.filter(uk_ogrn = '1103460001512').first()
pifset = PIF.objects.filter(Q(pif_uk = megainv) & ~Q(pif_checkpage=''))


#file_ = open('/home/ufk/monitoring_project/templates/solid.html', 'w')
#file_ = open('/home/ufk/monitoring_project/templates/openam.html', 'w')
#file_ = open('/home/ufk/monitoring_project/templates/tfg.html', 'w')
#file_ = open('/home/ufk/monitoring_project/templates/pragma.html', 'w')
#file_ = open('/home/ufk/monitoring_project/templates/veles.html', 'w')
#file_ = open('/home/ufk/monitoring_project/templates/rwminvest.html', 'w')
#file_ = open('/home/ufk/monitoring_project/templates/gamma.html', 'w')
#file_ = open('/home/ufk/monitoring_project/templates/rbcapital.html', 'w')
#file_ = open('/home/ufk/monitoring_project/templates/april.html', 'w')
#file_ = open('/home/ufk/monitoring_project/templates/navigator.html', 'w')
#file_ = open('/home/ufk/monitoring_project/templates/arsagera.html', 'w')
#file_ = open('/home/ufk/monitoring_project/templates/ew-mc.html', 'w')
#file_ = open('/home/ufk/monitoring_project/templates/ucnu.html', 'w')
#file_ = open('/home/ufk/monitoring_project/templates/kspcapital.html', 'w')
#file_ = open('/home/ufk/monitoring_project/templates/aricapital.html', 'w')
#file_ = open('/home/ufk/monitoring_project/templates/recordcap.html', 'w')
#file_ = open('/home/ufk/monitoring_project/templates/savingsim.html', 'w')
#file_ = open('/home/ufk/monitoring_project/templates/fdu.html', 'w')
#file_ = open('/home/ufk/monitoring_project/templates/olma-f.html', 'w')
#file_ = open('/home/ufk/monitoring_project/templates/trinfico-pm.html', 'w')
#file_ = open('/home/ufk/monitoring_project/templates/invest-ural.html', 'w')
#file_ = open('/home/ufk/monitoring_project/templates/oreol-2010.html', 'w')
#file_ = open('/home/ufk/monitoring_project/templates/redbridge.html', 'w')
#file_ = open('/home/ufk/monitoring_project/templates/leader-invest.html', 'w')
#file_ = open('/home/ufk/monitoring_project/templates/zaouk.html', 'w')
#file_ = open('/home/ufk/monitoring_project/templates/contrada.html', 'w')
#file_ = open('/home/ufk/monitoring_project/templates/veles-management.html', 'w')
#file_ = open('/home/ufk/monitoring_project/templates/tetis.html', 'w')
#file_ = open('/home/ufk/monitoring_project/templates/victory-am.html', 'w')
#file_ = open('/home/ufk/monitoring_project/templates/capital-am.html', 'w')
file_ = open('/home/ufk/monitoring_project/templates/megainv.html', 'w')

import importlib
#module = importlib.import_module('extractors.solid-mn')
#module = importlib.import_module('extractors.open-am')
#module = importlib.import_module('extractors.tfg')
#module = importlib.import_module('extractors.pragmacapital')
#module = importlib.import_module('extractors.veles')
#module = importlib.import_module('extractors.rwminvest')
#module = importlib.import_module('extractors.gamma')
#module = importlib.import_module('extractors.rbcapital')
#module = importlib.import_module('extractors.april')
#module = importlib.import_module('extractors.am-navigator')
#module = importlib.import_module('extractors.arsagera')
#module = importlib.import_module('extractors.ew-mc')
#module = importlib.import_module('extractors.ucnu')
#module = importlib.import_module('extractors.kspcapital')
#module = importlib.import_module('extractors.aricapital')
#module = importlib.import_module('extractors.recordcap')
#module = importlib.import_module('extractors.savingsim')
#module = importlib.import_module('extractors.fdu')
#module = importlib.import_module('extractors.olma-f')
#module = importlib.import_module('extractors.trinfico')
#module = importlib.import_module('extractors.invest-ural')
#module = importlib.import_module('extractors.oreol-2010')
#module = importlib.import_module('extractors.redbridge')
#module = importlib.import_module('extractors.leader-invest')
#module = importlib.import_module('extractors.zaouk')
#module = importlib.import_module('extractors.contrada')
#module = importlib.import_module('extractors.veles-management')
#module = importlib.import_module('extractors.victory-am')
#module = importlib.import_module('extractors.capital-am')
module = importlib.import_module('extractors.megainv')

for pif in pifset:
    start_time = time.time()
    ext = module.Extractor(pif.pif_checkpage)
    ext.scrape()
    content = ext.get_data(720)
    print(f'Execution time: {time.time() - start_time}')
    file_.write('<div class="container">')
    file_.write('<h3>{}</h3><a href="{}">{}</a>'.format(pif.pif_shortname, pif.pif_checkpage, pif.pif_checkpage))
    for e in content:
        if len(e) > 0:
            file_.write('<h5>{}</h5>'.format(e[0]))
            for k in e[1]:
                if len(k) > 0:
                    file_.write('<div class="d-flex flex-wrap justify-content-between">')
                    file_.write('<a href=\"{}\">{}</a><p><b>{}</b>'.format(k[2], k[0], k[1]))
                    file_.write('</div>')
    file_.write('</div>')
file_.close()
