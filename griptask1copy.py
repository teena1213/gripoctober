# -*- coding: utf-8 -*-
"""GripTask1Copy.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/12TocuyGfEv_R-mepFFyVY97dotA01RIb

### **SPARKS FOUNDATION_GRIP**

![GRIP.png](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAANYAAAD0CAYAAADnh9gTAAAAA3NCSVQICAjb4U/gAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAAEnQAABJ0Ad5mH3gAACgySURBVHhe7Z0HfBzVtf+PVtKqd8sV94IbhoBNJ5g/LaGEnuTx8gLhJYE8IAQCJHxoScgf8vIBAkkeAUJJSAiPEjAlNNNMszHGYGyKcbdxLypWr2++VztikbWzM6MdabU6X7NIO7uand29vznn/u65d9LaLURRlIQSivxUFCWBqLAUJQBUWIoSACosRQkAFZaiBIAKS1ECQIWlKAGgwhoA6FBl76MDxClGm/V1Nja3ye7GVqmsa5YdtS2yrbpJKmqapb41TayHLKGJhNPTJC8rJMU5GVKWlyFDCjOlKCfd2pYu2RkhCYXSJC2yT8U7KqwUgC+wpbVdtlviWbm9QVZuq5d1O+tly+4Wqapvk8aWNmlt41l7SsXSj2RnhqTQEtXggkwZWRyWsYOyZdLgHBlqiS0rwxJYmkrMKyqsFGBTVZO8ubJa3ltfK59XNkhdU7u0GCERnSxRdPwXE1qArZ2Q1TnItYQ2tDAsM0bkyuyJhTK6LMsSoIrLCyqsfgwp3/y1NfLweztkY0WTlQZ+IZCeQqNgVyW56XLy9FI5flqRFGZnmMeU+Kiw+hl8XVZmJ+t2NcpTH+6SN1ftlqaW9oQJqis0DvpjB4zMk1P2LbVSxGwJW30wxRkVVj+jgSi1Zrf8a1mlrLD6UpGML3Doi40syZITphfLVycUSn5WeuQRpTtUWP0IRPX00gp59qMK2VnTktDULx40El6qMDtd/t/ehXKqFb3K8jLNY8qeqLD6CU1W/jdnSYX8r9Wfam5t72zofUE4I02OnVwkZ88qN0JT9kST5X5Ac2ub6Us9vXSXERX0laiAPt28FdXyyvIqY6Aoe6LCSnJIKNbubJTnrPSvsr6VDR23aPog6ahpbJMXPq6UT7fWR7Yo0aiwkpxmS0uvWdFh1Y5Gk/4lE4yfPWeJq16j1h6osJKc1TsbrDSwWpqsFDANaeFWJMlgLebJonU1ZmBa+TIqrCSGur95n1VJRW1rpE8VJajolLAPhdZg9bfmflIpdU1WaFU6UWElMRV1rfL+hlojsD1Iosi1anuDbKhoitxTQIWVxGypbjKFtckM0q6z+lgbK5v6wkNJWlRYSUx1XaMppjXV5dGpX5JBRN1Vx4C1KstGhZW0WI20rU3a7ZqlJEr9usOuplc6UGElLWlSkheWjLTWpE+xQhxrdoapJ1Q6UGElMUOKsmVoUU7kXnKC5pkMOaw4syNlVQwqrCSmKCdDDhhTkMwZoGF4UVhGlWZF7imgwkpiWHeCKRqluRlJmQ5yTOmW6A+3jpG1M5QvUGElOaNLs+Ww8QWmojzZtEUgnTg4W746saBjg9KJCivJyUwXOXJioYwty4quu0gKinPT5YRpJVKq87L2QIWV5GAIjBuUZRow608kS9TCsJg9qVBmjc5POsEnAyqsfkBmekiOmFAgX59aYvo0fQ2NZr+98uSk6aVSoBMdu0VnEPcjmJ7x5JJdZmo+dYR8cb2pM14vHEqTA8fky9mzBqkT6IAKq59R39Qmr35WJU8vq+i1+jxeA8ufafi4lKfuWyKDC8OaAjqgwupn8HU1trTL0k118vgHu+Qj62fQi8qw65FWdDphWrEcPr7AjK8pzqiwXNLe2iotO3ZI88aN0rR1qzRv3ixtNTXS1tBgWnUoK0tCBQWSOWKEhIcOlcxhwyRj0CBjPgRFVX2LPPdxlTyzdJf1e0fpU6JfLmx1oQ4bXyhnfqVM9ioJ64q4LlFhdcF8HG1t0lZXJy2VldK0dq3Uvf++1C1eLA3Ll0vz9u3S3tTUUSDLc+2PjwbHLRSSUDhshJW9996SO3Om5Oyzj2SNGiWh4mLJyM2VtPTEdfipKF++tUFes9LDJRtrZXtNizRbEc1MlufQOCx+dyC6AfBc1uMsyM4wY1THTS6Sr4zM00U6PaLCioKo1PT550ZEtYsWSd0HH0jTunXSagmsvaXFiKlTQE7YHykLoVsiSispkaxx4yRsCazAElrhAQdI2BJeWkZiUipejgsfrK9olCWf15kFXjZYv1fVtUpjKxdEiDwxBpnpacY+J8Urz8+QsWXZMnVYjkwemiNFVr9KawC9o8IC6yNottK7qhdflKpnn5X6jz6SlooKkeaoSYZ+G5e1b/MB8/eWkEKWyPL320+KTzxRCo89VjLLyszTEgXLo1VaKeL23c2yuapZttU0yTtra2T19i8Wo+FnTmZIJg/JNnV+5fmZ5jI+iKo4N8MIDKFp2uefAS+stvp6qX7pJdl+991S9+GH0t7Y2PEAH0uCG5b5qK19EgFCVkqY+5WvyOD/+i/JP/xwkz4mio5vtEPQGBt/en2LzP20KrLdOgTrxpVEzj9iiLlUDwLirdrvViNUzxmwwjJp34YNsuPee2XXY49J665dptH3KtZHn15aKmXf+Y6U/fu/S9jqh6WRPiaQiroWuf6ZDbJ6R2Pn28sLh+TfZg0yLh+Dz0riGZDCIkrVzJ8v2/7nf6R24cIOMyIAUfHBxt2r9fGn5eVJ4ezZMviCCyTX6n8lytyg3/XP93fKo4t3miuUcDx4EEdOKJLvHDhIygu0xi8oBpywsMernn9ett1xh9QvXfqFIREAroQFiCszU3Ktvtewn/9c8g49tMeRi2Wp315dI/e8tdWsoMux0G86eGyB/NvMMhlh9a005QuOASUs0r/ql1+WTTfcII0rV5oGnTRwLFZDz5k2TUbcdJPkzZzpW1wdototf1+4QzZXNxtxY0xQ23f05EJTQaGiCpYBIyzeJvb551dcIfXLlkW2JiFWg88/7DAZfs01kjNjhmdx8T5f/LRKHnlvp9Q0thoRMQ511KRCmVieIxnJUMU7ABgwwmJ8av2ll0rNG29EtiQp1teRFg5L8ckny7BrrzXjXV5oa2uXlyxhsR7h8OKwjC7NkhHWzywd4O1VBoSwqKLYfPPNxlI3Y1PJngZZX0l6cbEMu+oqGXTuuZGN7uEK+nypGH46FtU3DIjTGCVJlXPm9A9RgXWMVHvs+OtfTU2iV0j3qKZQUfUdKS8solXVSy9Jy7Zt/UNUNtaxUptY+a9/mX6T0r9IbWFZDbLJOuNjWphav/6GdcxVlrBaq6oiG5T+QkoLi/N80/r15obI+h2hkDSsWmUKgZX+RWpHrNZWad60qV+f8Vt375bGNWsi95T+Qsqngm21tUZg/ZamJmnZuVP7Wf2MlDcvzJyofg4VI/0ylR3ApLawLFGlFxaaOrx+S0aGZBQXJ7zqXQmWlBdW5tChkl5U1L+s9ihCOTkS3muvyL3EQWrZ2t4iLW1N1s9maWuPM81Y8UTKV140rF4tGy67TGoXLIhs6UdYXw3rZYx76CHJLC+PbPQHIqpprpQtjetkU8NaqW7eJbUtVdLY1iAZaRmSnZ4vhRklMihruOyVM0FKwuUSDrFuoA4y+yHlhYV5seXWW005U3v0VPtkh68lPV2GXnGFDLnkEl/FuM3tjVLRtE1W1nwoK2s/lI11q4yYmolQsqehk2b9Q2RZoTwZnD1CxuVNl70L9pfBWSMlxxJeKE3TUbekfq2g9fZqFi6U9T/+sVlxqd+khNZxZ02cKOMeeMAsROMF0rvNDevk4+qF8snud2Vb4+fS3MaaF+2R+OP8GURW6RCrdydF4UEyIW+GTC86WMbkTZVsS3Q65SQ+A6MIt6FBtt5+u2y97baOSJDsWMeYZvWthl15pZSff76nGcWNrfXyzq4XZHHFqx2Cam+KCMq/GELWv6LMQTKlcKYcMegUky4qzgwIYQGrLq097zwzJT+p4euwhFR43HEy8r//WzKHDIk8EJ8qq9/07Ob7ZUnlm9IiTHBMZGShmaTJiOzxctpeF8io3L0TvP/UYsAkzRklJWYaRvbkyR3pYLKeT6y+FBMcy62TACvpugFHb4uV+s3ZeKcsrpxn9Z5aAmj0Hfvb2LBSHtlwuyytmm+ll01mm7InA6o3ynJjQy69VLLGj5d2qwEno7SyJkyQwRddJHkHHeQ6Baxo2iqvbHtUPt29yLoX9LtKMynm3K3/kJU1S6S1vR9XtQTIgBIWA8VFxx5rxJVhNeBWlomOPNanED2tW9bYsTLciqpFxxxj1oJ3Q5vVsBdWzJWPqt+RlvbecT3ps21t2CBv7HhKdjVuiWxVohlw/ikDrsXf+IbsdeONkjN9urA8Z2tfpoW8thU9WfZs1G23SeHxx0soOzvyYHzW1S2Xd3a+IE1t9ZEtMeAt2rceQprJ6vCra5bJe5WvRLYq0Qy8gQmrfxWyIlfJEUfIuHvukUFnnSXpLPPc2/0uXst6Tabgl5xxhoy89VbJnTXLswM4b9vjUttK9X7vGwkYJIsrXjOpofJlBowr2B28da4eUv3882bqft2SJR3V8JFGHwiRfbPEdPbUqVJy+ulSdMIJxv3zOj60YvcH8td1N0pjW511r/eFBdY7ka8N/Y7MLj9DB5CjGNDCMlhvv62xURpXrZLd8+aZCyOwPBrXvkqowCIfc5rVd8KZLDruOCk8+mgjLrf9qWj42l7d9pg8t/WByJYY8LIBao7+1uSCmfLd0T+XcMh9CpvqqLAi8DFQ8sTF5WrfeUcqn37a1Be2MEnSXoTGj8hYaddK79Lz8yVryhQpOeUUKTzqKMkcPtyIzG8VA6bFExvvlAW7no9siUEvCGtweKRcMP7/S2FmaWSrosKKASJjWjziYn13FnZp2bVLWolk1mPMkeq29pCPk6kepaXmFh4zRnL33VfyDznEjE+l5+VFntgzENacTXfL/J3PRrZ0vDT/SwsFqKQuIKzy8Aj54bhfm8JdpQMVVhxMJGtoMJUbXJ3ETPWvrjZ1hzsffLBj2n901LGez8DukMsvN9e/Yi4V/alEz6eiQb++fY48s/l+c89s6yNhjcmdKv859nrJSU/MSSMV0N5mHEjVzJwoK3XLP+ggKTn1VCn7j/8wY2Fl55xj0rmOFv0FrbW1Zl3A8JAhJgUMYpIiljfTO8JpWaZx8x9y6u0CWY5jbN4UydL+1ZdQYXnFargIhZnJQy6+2Iw70YfqFJf1OBGu4oknpDHg1ZWG54yTkVmTjKg66VVdtUtueqHMKDpcQmmJufRQqqDC6gGIa+iPfyx5BxzwZXFZNK5YIdvvusssGBpUtk3qdUT5KWYqh4lavSgqXg+rfVrhgbJX7vjIVsUm/RcWkd8VH2SUlUl45Ehp3rKlYzloFn4hHbPE1PDppya65UyebKaBBJGmlWYNlsrmHbKlYb3V1Htren3HNJTh2WPluKFnS3GmmhZdUWH1EIQTHjFCcqZONVeGxODovI6xJbKGzz4z7iGFvyH6WwkWFylYcbhcdjZtNrOFTeQKGGRVaonpqMFnyqT8/TQN7AYVVgKgDCmjvFzyDz5Ysi0BYcszHsYS0VyWlavwsxpvzsSJJsKZiJZA8jIKpSxruGxtXC9VVvQKEoSbn1EsR5afLvuXzJbMkP+xuFRG7fYEw8fJApuUSe16+GGpX768c9FQLt49+MILpeikk4wNT/FtIhvlpvo1ZtB4fZ31msLlUTtStp5i74d/JeHBcsLQc2WfokM0UjmgwgoKBFZZaS7IUPvee9JA1Fq3zlycIXfmTBn0ve+Zy6Im2oqvbNou83bMkWVV86W6eaclr1YjCL/YJkVeeoFMyN9XDh/0DRmdN8lsU2KjwgoYPl76WK1Weoi50bxtm6lNzJkyxfS7ghjjqm2pluW7F8vSqrdkTd0nUteyu3NVJrcis6NUVihHhmePk32KD5WphQdafavBVpRVUcVDhdXLmI+bm5UCmiYeQP8EUVDyVNNSKZvr18qKmg9kTe0nsqNpkzS01lmPIrIvvy5/A0SizLRMq99WJCNzJ8qUglkyNm+qWUwmI5RpxKbER4U1AOArbmirl+2NG2Tl7g/l9Z1zLNFVdYok3fo3JHu0DM0eZUyQETljTJQqzCiVdEtMindUWAMIvupVtUvlgXU3Sl1rTURWaTK14EA5efh/Skl4iBWvEmuoDFQ0WR5AVLdUyBs7npT61trIljQZnbO3HD3kW1IWHibpaekqqgShwuonEG3q6+ulubupKi6otyLUgp3PyordS0x/KmSlfywhffLwH5hiXhVUYlFh9ROWLVsm5557rlx33XVSWVkZ2eoOXEJWVHprxzPS1N4gmWlhMw51xogLZVTuJJ1SHwDax0oy+DpqmXbS2ir5+fmSnp4ujY2NcvPNN8uNN95o7v/lL3+R0047zUQZnt/W1iahLoPNbG9qazROIOnfJ9WLrFQvZC5wMKP4CNmn8BDJzyzqNDCUxKKnqiRj27Zt8tvf/lauueYaWbp0qdnW1NQkGzduND8bGhrks88+M8JDUB988IH84x//kI8//lhaWlrM84E1BlfVLumYYWyJ7JCyr8npVoQ6e9Tlckjp16Qgs1hFFSAqrCQD0dx9991y1113yZw5c8w2RISo7Oi0fft2s23Dhg1y6aWXmttvfvMbI0ob0rth2WNldvnpVj/q+3L04G/KtMKDzLoU2p8KHhVWEoJ4MCkWLVpkfo/O1vl99+7dZvvKlSvl7bfflp07d5qfCM0mPS3D1PVxZRCKdLVYtndRYSUZpaWlkpOTY35ftWqV7KBKvgv0uYhYu1jcxvoJRDRcQyU5UGElGUVFRTIocpWRzZs3myhkGxNEK25EM26Izo5mPK4RKXlQYfUhpHM1NTVfGpvKzc2VvSIX866rqzN9Lls0tnAwKey+lk1GRoZke1jzXQkWFVYfsn79evnRj34k9957rxEYZGVlyejRo41QSPNsZzA6GiEsblu3bu2MWPwdolSSAxVWH4I58eijj5oxqvnz55solJmZKWPGjDHRh/vLly83EY3xKxu2E82iIxZjXohLSQ5UWD2EiEFDtyOHF0aOHGkEQeR69tlnjfmAgEaNGiWFhYXmOTh/VFpEDwATyaqqqkzEsikuLlZhJREqrB6CwcAA7RtvvNHp0Lll2rRpcsghh5i0bu7cubJmzRojoOHDh3caGIxN8Rpgixch4whGRyyEpX2s5EGF5RHEgxDsRv7444/LZZddZioloiOIG/Ly8uRb3/qWsddXrFhhohZRCZHYwqLvheCiDQ6OAbeQ8SxAjCUlJRIOh819pe9RYXmABn377bfLVVdd1RlFSOMqKiqMyfDJJ5+YaLJ69WojuLVr1zqmiIjosMMOk4kTJ5pxqL///e/y+eefm/SwrKzMCIYxq08//dQIjH1x43dKmGxh0S9j/MsWFs/hOEgtiWx21YbSe6iwPICY/vSnP8mDDz7Y6dbZIADq+Wj0f/zjH+W73/2uXHnllcZkcGLw4MFy5JFHGnEglj/84Q9GBPSxEB7R8cknn5QFCxZ0imPJkiXyt7/9rdNJxEFEWPwEjuXVV1+VSy65RL7+9a+bol3EpfQeKiwP0GARClEAUyEaBFBdXW2iBI/xPFw/yo2coF80e/ZsKS8vNxER0f7zn//snBqCmD766CMTBW1hIShEbvfpEBTpoy2sl19+2Yj6/vvvl4ULF8rrr7+uVRm9jArLA0SFIUOGmP4O5UZdIf2i+hzDARHQ8NnmBOnePvvsI1OmTDERatOmTWZ6CGaGLZx4EO1IH/l7hIx9T9U7YsdlPPDAA6WgoCDybKU3UGE5gDgQEQ2c3yk3YvAWsZAKso3GDDyHSEZkwAq3sR+PBY/jAu63334m4rBPxEH0cwvisftXTzzxhCnItQW9//77y5lnnvmlcTAleFRYDhB5brvtNhM96KMQXRhj4ieRBQGRykWLi3TR7s/Q2O30zAn2MX36dN92OSLitbHfqeKwX5/0khnHCFfpXVRYDuDQYUTgBOL+AQ4eA7FEFSxvUiyEBgiM2b+IC0gbsdTjwd/jAvq1y0k/MU5ee+01kwIC6eEpp5wiRx99tLmv9C4qLAdo7JgClBvNmzfPbCNiEVmIVpQbRUckhIWpYLt1RAq39XvsxxaoVxDzI488Ir/73e+MyGDSpEnyPZaxjkxBUXoXFZYDRByMBfo7jEuRbjFwi9hItxjU7QrunW2xDx061HUUimdyOMHfvvPOO+YGiPSoo44ylR1K36DCcoB06phjjjHp3rvvvivvvfeeiWKIi8a8ePFiMziM4cDNHrjFjSN60ceJhr8hTYyu3LDh+V23+QXhz5o1yziFXaE65M477zQpI8fDa9rpa6JeX1FhOWJb1Zz5ERBrUeAS0nARAhHipZde6hTK888/L6+88or5nUg1YsQIsx/uY4Q8/fTTZgCY53UdVyJlQ8iJYNiwYSbSducEPvfcc3L11VfLAw88YCo3cDJvueUWeeaZZzr7hkrPUWE5gHioQD/iiCNMekU/5r777jOpIWLB3GAA1k7jKGmyTQ6EQn8MMDmuv/56ufDCC+VXv/qVGbjtOnCMCLHzE8HUqVPN1BPgRICpwWA16StlVgw+c6ycLCiXQuwPP/ywEZmSGFRYcSCdOvbYY00U4Az/+9//3jRSQFxEKxvu2xAtSBmJAowtUQGPc4e5gOCIetEwa3jfffeN3PMPBgj9K3v/VN2fddZZcvnllxtR2QPJiB1hITJSQURlGx9Kz1FhxYFGOHnyZGOzAwYGt3gQ4UgHabCki3bBLAPMZ5xxxh6VELiHCKC7fpEXxo0bZyx2jhsQM6+N0UK1CK9PyomYcDbtflY0nAwQWdftintUWC7AhEBcXiCScaPO7/333zeNFKGxTDTGQncQGb/5zW/6Hs9izIyp/mPHjo1sEfM7aamd9jEEgOgxWhhQtsWD2Ih2nDRwQEl7EZ/iDxWWC0jrvNba0XCpSqdPtmXLFrPtq1/9qhlbijXTl4r2K664wkQcGr8XEM+3v/1tI9xo04IIxVwtohBV8fTjECBDAvbUF6Ib74/jQmyYGY899pgRo+IPFZYLaHh2auUWGvJNN91kGihRgIZ//vnnm76aEwzsMnHSTj3dwBDAxRdfbIwRRBQNY3Hsi5QPi533YRcS28unsY2IhSCJrgx8k5JyzIo/VFgBgqVOAwYEdcABB8QVKOkY6RqDy25gvwwD/OIXvzB/13X/pJW4hERAzAucTJ5HmsrvmBe2q4nIEBbHjMHiphxL6R4VlgtorPbiLn4hahBZ3EBDtxt7PA4++GA58cQTHaMLlfOIBBMDlxBhAWYGA8a8Fu+R1O+tt94y0QsTxG9fTxmgwrKNBbcQRZgv5bXfY0NDnTFjhuvqdVJHO9LFg9SP/TtBeomYEBAOJeNZCAmn0F4Eh230wTBbECF9s+4GmBV3DDhh0WlnWjuXyvHieiGMaLfNC4xnsbaFW2EiALfCRwRd0z/6d0QnO+qRLo4fP948jzIsqix4DFPlhRdeMMJCVAwUY2gwodMeYFb8kdLCos/AvClcLsREY6VjzlQQLntDZ57n0BDjRQj6HD/84Q89z5nCacNGpzTKTfU6x8OxuI1YHE+0sDhx/OQnPzFrXXDyYKyKqMZ8LyIb+42e9m+/DktZkwYSuTgRuE1ble5JaWFxVma6Bw0MITFYy1iOXXZEg8QZu+eee+Shhx5yjBI8Fyv7pJNOct33wMI+9dRTjcuHE+cWt8LimLr2rThJUCyMSG644Qb59a9/bd4XEcutGYGo/E66VDpIaWHROIlQdMqpJEBo3OcsjhlBioQLRkQjDYq34ApnclY+os8SD/o0P/vZz4ygKYh1E61s3ERQYJ9dBcD7Ovvss006R/T685//bGZAczxuDRiiFumh4p+UFxYlPZyxiR4ICyeM+9jZnJnpvGM7U1vnZolmOvUU5kanX11hEJbaPFIynu9FVKRnNGy3EavrMWM4MFB8+umnm8c4iTBdn5Wj2LcbiOK6qlPPSGlhcda1qwdImWiw9iKaRB0E9uabb5rnzZw5M2H2Mn0aFnGh/s9JgLFwG7HYd3fHTNp5wQUXmH4V8B5Jh+0KkHjQB4tevlrxTsoLy57iQWNHZJgZuHPY50ydYLUlUjwWzeR5RDVubs/u3YGIe1K14EVY3VntbKdSnrpBhEcaTOTmxOIG3FLb4FD8kdLCQiD2+hM0QBoX86CIJEQs1kqnAVGZgNAQIivIMlmRxt0dCM7J5ACE63cMiP0jADciiCUs4BhwBqn28ArlTPTRFP+kjLDsSBMN4ojuK9jrUdBoiCgICwFQbU5/C/v9pz/9qansjtXH4DUQoFNEo2/jpr/WHeyXCBNPvDZOg8P0I/0MEdAvjFfTqDiTEsIi6mBpn3POOSbicLangSIs+8xPQ122bJn5iUPGRD+sd0TGGBNiwZpmPIeG5dQYnUQFuG9++1fsG/F3PUl0B/t3ioyYJpgYlD25hRMC88W6FvMq3kgJYbGexFNPPWXWPb/ooovkxRdfNEKhgdqRB1eMTjwNl7M8q8USGZi5yxgPUYoqBGrk6G/FEhb7xGmLhd3Y/YgKEJRbYUG8lBORf//73zdOphsOPfRQI0a/x690kBLCIuWhn4RoiDiIDEHRCaeRAnVxjGEBkYp+FI2HigocMNahQIysyoSbFqthsV97n0HAe+A13EYsN1Y+lR+khERiJ8HwGGNumDlKz0gJYTFGxQXcSGNI9XD6EBWCsafE02DtxkpFN9YzDYlqjFtvvdXU0FGBTnWF06IuuHVuHDu/cIwcOyJ3gxthMQOahWzuuOMOOe2002JGOT4jxrDcvrYSm5QQFgJh6oQ9fX7dunXGVsdOdxIBjZiSJ1JAoJ/GFAuns3p0ehkEXoXlBt4PfaYTTjjBLIbjVGDLuog6c7jnpISwABOClIezMVGIdfPoN8WLLpylaXhMh+eqHPGg4duRLxaMHfmdYsLxeOlj8XwvcKE7+pSxoLrd6yVflT1JGWEBqRyNGjfwrrvu6rxAQDxw8BCVm3X9MDxijXHZ9ERYCMptHw5ReY1sGDf0R2OlgzisRHqlZ6SUsIhadp8DAbhtdPyd23XO3USsnsAxezFHvEYscJq0yfAEkx2DfI8DgZQSFhUD3dXOxYP0yO38I/o/QTY6zBdeI0joY8VadQqhYuTYFSuKP1JKWAjEy7wnG+x6t3OVgnQEAWF5iVhORkssWM666wUbolmzZo1xBxX/pJSwGARlCrxTmU9X6F9RiR7rDN4V+iA0/qBAuEFHLKbI2AvKdAeiovxL8U9KCQtLmQUx3U6DBxyy448/3nU1OilSkOM89HG82Pl++licTJzmidlLUgf5PlOdlBIWThd1cddee62rEh7Sv/POO89UgLsVItXxQUYs0kA3le09gYF0IlasyI7rSXUKBpDij5QSFv0NxEVZElPonSxvnMBf/vKX8oMf/MBT9Xf06kdBQET0Iiw/UQWDhxWnYvUrOXEw05rxQMUfKSUsG8RFiufU1+JSN5T5uDUtbII+iyNcL8Lykwry+RCxnJxBqv8ZKPazfyVFhQV0wGM1UCLbhAkTPM9TgqBdQSKWl9fwGz1xT4nasWDGAGuBqLD8kbLCojQnVppEKmRfxtQL7C9ox46IFa+yw4ZG70dYnFgQFVXssex6psZgYAR9IklVUlJYNAZSmVgQqZzs5ljQ9wg6FWSNDi9i8evcUb7FZxBLWLxPKjDcilz5MikpLBqDk7Cw1hlM9grRquu1gxMNleWxGntX/EYsoG/pZLmzb+av2dNuFG+kpLBoDE7Ld5EGuSm47QrjS06zhxMBA9Be+jV+IxaOKaVNTgYPFRgsF6d4JyWFhXHhZBVTF+h2Vdho3M4eJo3y0zdBUF7mQvF8v8IiKrIMgZMrymfISsGKd1JWWE6RhQoNP6soIRY3DZm+mN8Gb6+D6Ba/rwPUCzoJi/e7aNGiQMftUpWUExaNEps4ltVOnwI3zEs9oQ3RKsiqC/bdWxEL6GfGq1Ch0l0Lcr2TcsKioXE1ESdhkQr6mV5CKhiksEghvdr5PREW6bDTbGLABNKJj95JOWERVYhYsQRA1QFnaj8RC2H1pCHHg2P3IiwiVk+EzmfAilR8JrEgNV24cKGmgx5JOWFRuYCwYgmAvhXTJpwaUywo8QkyYiFcrxGrJ8eDgcECPE4nGQS1YMECV6aN8gUpJyzsaqz2WAYAY1gIy201ezSkmEFWIvR2xAIs93gOKZXuTuOCyp6klLBoaAzgOlntVF0whuVVWOwb0QaZEiEsL5EhEcKi+iLerGvqBilvinWyUvYkpYRF+scVRZycNSb5cYZ2W91gQ6MKeh0IP1NSeiosPot4ziDvm3Xvg4zWqUZKCYsvnpTFSQAsOEM66EdYRKx48DyijpepHzZey6USEbGowMDAcIrgfK4s5Bl01UkqkVLCovPPWg1O00WYg+R1DhbQiN0W4OKkIW7+xgsI16vrmIjUlEmPTpNCOSY+V1JCr+9poJJSwiJSUN/m1NgQFemgV2hcCNcNND4/DZCI1dupICCseIvp4LSydLcKyx0pJSzcQJy7WBCx6FP4KWei/8MZO0j8mCNE5542di4yh1PqBKJnoDgRQh4IpJSw6F9hXsSCsSvqBP1UXZAGuulj+YWI6Gf/NPSeCivecmhAtNb5We5JKWFxbSynL54OOo3Ib52gF1fQqzmCQeBn7lMihEVqzKKlTsfMa3B5JDUw3JEywiKF4ot3cuMQFhHLj7CIWG7NC6KPVxOC4/bTaPm7nhoYRHAilpOBAczN4sqYSnxSRlhEEyxhp7M3DYeI5TWaAA3YbRpE2uTW6LDxK6xERCz6nIxlxUuRSVXffffdyD3FiZQRFv0rHEEniFRELD/CotTIbQPmeV4jFqkgNr1X+LueCosTDtUX8VatQsRvvfWWeU3FmZQR1pIlS+L2UeyI5QevxbFeIcJ5KWeySUQqSIpMKuhmuQI+Z6x3xZmUEBbRgZmuNDIncAX9rHUB1B/2tAE7wUnBa5SDRKSCRHAmfxLN48G1m3W6fnxSQlhEE86k8WBw2G/VBcJy2/D9NHT6iH5SrEQIC4jkTNWPV5xMP3P+/PmaDsYhJYTFhbxZazweRCs/wiJSMUDqtgEjQK8Nj4jlZ4woEakgEK0YKI4nLD6Dt99+W6frxyHN+qB6frrrhrlz50Z+CxbSGFKT6667Lq4dPmPGDLn++utN9YXbt83+Ecp9991nLhbuBpZX4wr8Bx10kKvX4TXefPNNueWWWzyNlQGXPb3pppvMCaMnXyUngvvvv1+efPLJuCcF+mNXX321TJo0qUevGSRc6L0vCUxYfiKDXzhjuxlj4myMtezHFSQykHa5gf1jXfN6bl+LfcfrI3ZHT95TNDQDBOX2PfKafmZh9xZBm03xCExYPf2iFaUnBNSsXZMSfSxFSTZUWIoSACosRQkAFZaiBEBg5kW8lX8UJUhYA7IvCUxYTIpTlL5i2rRpkd/6hsCEpSgDGe1jKUoAqLAUJQBUWIoSACosRQkAFZaiBIAKS1ECQIWlKAGgwlKUAFBhKUoAqLAUJQBUWIoSACosRQkAFZaiBIAKS1ECQIWlKAGgwlKUAFBhKUoAqLAUJQBUWIoSACosRQkAFZaiBIAKS1ECQIWlKAGgwlKUAFBhKUoAqLAUJQBUWIoSACosRQkAFZaiBIAKS1ECQIWlKAGgwlKUAFBhKUoAqLAUJQBUWIoSACosRQkAFZaiBIAKS1ECQIWlKAGgwlKUAFBhKUoAqLAUJQBUWIoSACosRQkAFZaiBIAKS1ECQIWlKAGgwlKUAFBhKUoAqLAUJQBUWIoSACosRQkAFZaiBIAKS1ECQIWlKAGgwlKUAFBhKUoAqLAUJQBUWIoSACosRQkAFZaiBIAKS1ECQIWlKAlH5P8AaRXGi3wL3gQAAAAASUVORK5CYII=)

### **#GRIPOCTOBER21**

## ***Author Name:TEENA JOSEPH***

## **TASK1: Prediction Using Supervised ML**
## **Predict Percentage of students based on number of study hours.**
"""

# Commented out IPython magic to ensure Python compatibility.
#IMPORTING LIBRARIES

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline
import statsmodels.api as sm

#READING DATASET FROM URL

url="http://bit.ly/w-data"
dataset=pd.read_csv(url)
dataset

#Exploring nature of DATA

dataset.shape

dataset.head()

dataset.describe()

#Regression
y=dataset['Scores']
x=dataset['Hours']

#Explore data
plt.scatter(x,y)
plt.xlabel('Hours',fontsize=15)
plt.ylabel('Percentage',fontsize=15)
plt.grid()
plt.show()

x1=sm.add_constant(x)
results=sm.OLS(y,x1).fit()  #The result will contain the o/p of the Ordinary Least Squares(OLS) Regression.
results.summary()

#Apply output to equation and rerun the code
plt.scatter(x,y)
yhat= 9.7758*x+2.4837
fig=plt.plot(x,yhat,lw=4,c='orange',label='regression line')
plt.xlabel('Hours',fontsize=20)
plt.ylabel('Scores',fontsize=20)
plt.grid()
plt.show()

#CORRELATION
dataset.corr(method='pearson')

dataset.corr(method='spearman')

#Linear Regression
#using iloc function we divide the data

X=dataset.iloc[:,:1].values
Y=dataset.iloc[:,1:].values

X

Y

#Splitting Data into training and testing

from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2,random_state=0)

#Training our Model

from sklearn.linear_model import LinearRegression  

model = LinearRegression()  
model.fit(X_train, Y_train)

#Visualizing train data
line = model.coef_*X + model.intercept_

# Plotting for the training data
plt.rcParams["figure.figsize"] = [14,7]
plt.scatter(X_train, Y_train, color='blue')
plt.plot(X, line, color='orange');
plt.xlabel('Hours Studied',fontsize=20)  
plt.ylabel('Percentage Score',fontsize=20) 
plt.grid()
plt.show()

# Plotting for the testing data

plt.rcParams["figure.figsize"] = [14,7]
plt.scatter(X_test, Y_test, color='blue')
plt.plot(X, line, color='orange');
plt.xlabel('Hours Studied',fontsize=20)  
plt.ylabel('Percentage Score',fontsize=20) 
plt.grid()
plt.show()

#Making Predictions
print(X_test)
y_pred=model.predict(X_test)

# Comparing Actual vs Predicted
comp = pd.DataFrame({ 'Actual':[Y_test],'Predicted':[y_pred] })
comp

"""
What will be the predicted score if a student studies for 9.25 hrs/day?"""

# Testing with your own data
hours = 9.25
own_pred = model.predict([[hours]])
print("The predicted score if a student studies for",hours,"hours is",own_pred[0])

#MODEL EVALUATION
from sklearn import metrics 
print('Mean Absolute Error:', metrics.mean_absolute_error(Y_test, y_pred))

