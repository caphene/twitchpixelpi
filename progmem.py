# Replicate progmem Arduino sketch
# Usage: progmem.play(game, frame)
# Will return 256 element list of tuples for RGB values

import re

DigDug01 = ['#000000', '#000000', '#000000', '#000000', '#000000',
            '#000000', '#000000', '#000000', '#000000', '#000000',
            '#000000', '#000000', '#000000', '#000000', '#000000',
            '#000000', '#000000', '#000000', '#000000', '#000000',
            '#000000', '#000000', '#000000', '#000000', '#cccccc',
            '#cccccc', '#cccccc', '#000000', '#000000', '#000000',
            '#000000', '#000000', '#000000', '#000000', '#000000',
            '#cccccc', '#cccccc', '#cccccc', '#cccccc', '#cccccc',
            '#000000', '#000000', '#000000', '#000000', '#000000',
            '#000000', '#000000', '#000000', '#000000', '#000000',
            '#000000', '#000000', '#000000', '#000000', '#cccccc',
            '#cccccc', '#cccccc', '#cccccc', '#cccccc', '#cccccc',
            '#cccccc', '#cccccc', '#000000', '#000000', '#000000',
            '#cccccc', '#cccccc', '#cccccc', '#cccccc', '#cccccc',
            '#cccccc', '#cccccc', '#cccccc', '#cccccc', '#cccccc',
            '#cccccc', '#000000', '#000000', '#000000', '#000000',
            '#000000', '#000000', '#000000', '#000000', '#0066cc',
            '#000000', '#0066cc', '#000000', '#0066cc', '#0066cc',
            '#0066cc', '#0066cc', '#cccccc', '#cccccc', '#cccccc',
            '#000000', '#000000', '#cccccc', '#cccccc', '#cccccc',
            '#0066cc', '#0066cc', '#0066cc', '#0066cc', '#000000',
            '#0066cc', '#000000', '#0066cc', '#000000', '#000000',
            '#000000', '#000000', '#000000', '#000000', '#000000',
            '#000000', '#000000', '#0066cc', '#0066cc', '#0066cc',
            '#0066cc', '#0066cc', '#0066cc', '#cccccc', '#cccccc',
            '#cccccc', '#cccccc', '#000000', '#000000', '#000000',
            '#000000', '#0066cc', '#0066cc', '#cccccc', '#cccccc',
            '#cccccc', '#cccccc', '#cccccc', '#000000', '#000000',
            '#ff0000', '#000000', '#000000', '#000000', '#000000',
            '#000000', '#ff0000', '#ff0000', '#000000', '#cccccc',
            '#cccccc', '#cccccc', '#cccccc', '#cccccc', '#cccccc',
            '#0066cc', '#0066cc', '#cccccc', '#000000', '#000000',
            '#000000', '#ff0000', '#ff0000', '#ff0000', '#0066cc',
            '#0066cc', '#0066cc', '#0066cc', '#ff0000', '#ff0000',
            '#ff0000', '#ff0000', '#ff0000', '#ff0000', '#ff0000',
            '#000000', '#000000', '#000000', '#ff0000', '#ff0000',
            '#000000', '#cccccc', '#cccccc', '#cccccc', '#0066cc',
            '#0066cc', '#0066cc', '#cccccc', '#cccccc', '#000000',
            '#000000', '#000000', '#000000', '#000000', '#cccccc',
            '#cccccc', '#cccccc', '#cccccc', '#cccccc', '#cccccc',
            '#cccccc', '#cccccc', '#000000', '#000000', '#ff0000',
            '#000000', '#000000', '#000000', '#000000', '#000000',
            '#000000', '#000000', '#000000', '#000000', '#000000',
            '#cccccc', '#cccccc', '#000000', '#000000', '#000000',
            '#cccccc', '#cccccc', '#000000', '#000000', '#000000',
            '#000000', '#cccccc', '#cccccc', '#cccccc', '#cccccc',
            '#000000', '#cccccc', '#cccccc', '#cccccc', '#cccccc',
            '#000000', '#000000', '#000000', '#000000', '#000000',
            '#000000', '#000000', '#000000', '#000000', '#000000',
            '#000000', '#000000', '#000000', '#000000', '#000000',
            '#000000', '#000000', '#000000', '#000000', '#000000',
            '#000000']

DigDug02 = ['#000000', '#000000', '#000000', '#000000', '#000000',
            '#000000', '#000000', '#000000', '#000000', '#000000',
            '#000000', '#000000', '#000000', '#000000', '#000000',
            '#000000', '#000000', '#000000', '#000000', '#000000',
            '#000000', '#000000', '#000000', '#000000', '#cccccc',
            '#cccccc', '#cccccc', '#000000', '#000000', '#000000',
            '#000000', '#000000', '#000000', '#000000', '#000000',
            '#cccccc', '#cccccc', '#cccccc', '#cccccc', '#cccccc',
            '#000000', '#000000', '#000000', '#000000', '#000000',
            '#000000', '#000000', '#000000', '#000000', '#000000',
            '#000000', '#000000', '#000000', '#000000', '#cccccc',
            '#cccccc', '#cccccc', '#cccccc', '#cccccc', '#cccccc',
            '#cccccc', '#cccccc', '#000000', '#000000', '#000000',
            '#cccccc', '#cccccc', '#cccccc', '#cccccc', '#cccccc',
            '#cccccc', '#cccccc', '#cccccc', '#cccccc', '#cccccc',
            '#cccccc', '#000000', '#000000', '#000000', '#000000',
            '#000000', '#000000', '#000000', '#000000', '#0066cc',
            '#000000', '#0066cc', '#000000', '#0066cc', '#0066cc',
            '#0066cc', '#0066cc', '#cccccc', '#cccccc', '#cccccc',
            '#000000', '#000000', '#cccccc', '#cccccc', '#cccccc',
            '#0066cc', '#0066cc', '#0066cc', '#0066cc', '#000000',
            '#0066cc', '#000000', '#0066cc', '#000000', '#000000',
            '#000000', '#000000', '#000000', '#000000', '#000000',
            '#000000', '#000000', '#0066cc', '#0066cc', '#0066cc',
            '#0066cc', '#0066cc', '#0066cc', '#cccccc', '#cccccc',
            '#cccccc', '#cccccc', '#000000', '#000000', '#000000',
            '#000000', '#0066cc', '#0066cc', '#cccccc', '#cccccc',
            '#cccccc', '#cccccc', '#cccccc', '#000000', '#000000',
            '#ff0000', '#000000', '#000000', '#000000', '#000000',
            '#000000', '#ff0000', '#ff0000', '#000000', '#000000',
            '#000000', '#cccccc', '#cccccc', '#cccccc', '#cccccc',
            '#0066cc', '#0066cc', '#cccccc', '#000000', '#000000',
            '#000000', '#ff0000', '#ff0000', '#ff0000', '#0066cc',
            '#0066cc', '#0066cc', '#0066cc', '#ff0000', '#ff0000',
            '#ff0000', '#ff0000', '#ff0000', '#ff0000', '#ff0000',
            '#000000', '#000000', '#000000', '#ff0000', '#ff0000',
            '#000000', '#000000', '#000000', '#cccccc', '#0066cc',
            '#0066cc', '#0066cc', '#cccccc', '#cccccc', '#cccccc',
            '#000000', '#000000', '#000000', '#000000', '#000000',
            '#cccccc', '#cccccc', '#cccccc', '#cccccc', '#cccccc',
            '#000000', '#000000', '#000000', '#000000', '#ff0000',
            '#000000', '#000000', '#000000', '#000000', '#000000',
            '#000000', '#000000', '#000000', '#000000', '#000000',
            '#000000', '#000000', '#cccccc', '#cccccc', '#000000',
            '#000000', '#000000', '#000000', '#000000', '#000000',
            '#000000', '#000000', '#000000', '#000000', '#cccccc',
            '#cccccc', '#cccccc', '#cccccc', '#000000', '#000000',
            '#000000', '#000000', '#000000', '#000000', '#000000',
            '#000000', '#000000', '#000000', '#000000', '#000000',
            '#000000', '#000000', '#000000', '#000000', '#000000',
            '#000000', '#000000', '#000000', '#000000', '#000000',
            '#000000']

Qbert01 = ['#000000', '#000000', '#000000', '#000000', '#000000',
           '#000000', '#000000', '#000000', '#000000', '#000000',
           '#000000', '#000000', '#000000', '#000000', '#000000',
           '#000000', '#000000', '#000000', '#000000', '#000000',
           '#000000', '#000000', '#000000', '#000000', '#000000',
           '#000000', '#000000', '#000000', '#000000', '#000000',
           '#000000', '#000000', '#000000', '#000000', '#000000',
           '#000000', '#ff6600', '#ff6600', '#ff6600', '#ff6600',
           '#000000', '#000000', '#000000', '#000000', '#000000',
           '#000000', '#000000', '#000000', '#000000', '#000000',
           '#000000', '#000000', '#000000', '#000000', '#ff0033',
           '#ff0033', '#ff0033', '#ff0033', '#ff0033', '#ff6600',
           '#ff6600', '#ff6600', '#000000', '#000000', '#000000',
           '#ff0033', '#ff0033', '#ff6600', '#ff0033', '#ffffcc',
           '#ffffcc', '#ff0033', '#ffffcc', '#ffffcc', '#000000',
           '#000000', '#000000', '#000000', '#000000', '#000000',
           '#000000', '#000000', '#000000', '#000000', '#000000',
           '#000000', '#000000', '#000000', '#ff0033', '#000000',
           '#000000', '#ff0033', '#ff6600', '#ff6600', '#ff0033',
           '#ff0033', '#ff0033', '#ff0033', '#ff0033', '#ff6600',
           '#ff0033', '#ff0033', '#ff0033', '#ff0033', '#ff0033',
           '#ff0033', '#ff6600', '#000000', '#000000', '#000000',
           '#000000', '#000000', '#000000', '#000000', '#000000',
           '#ff6600', '#ff6600', '#ff6600', '#ff6600', '#ff6600',
           '#ff6600', '#ff0033', '#ff0033', '#ff6600', '#ff6600',
           '#ff6600', '#ff0033', '#ff0033', '#ff0033', '#ff0033',
           '#ff0033', '#ff6600', '#ff6600', '#ff6600', '#ff6600',
           '#ff6600', '#ff6600', '#ff6600', '#ff6600', '#ff6600',
           '#ff6600', '#ff6600', '#000000', '#000000', '#000000',
           '#ff6600', '#ff6600', '#ff6600', '#ff0033', '#ff0033',
           '#ff0033', '#ff6600', '#ff0033', '#ff6600', '#ff0033',
           '#ff6600', '#ff0033', '#ff6600', '#ff0033', '#ff0033',
           '#000000', '#ff0033', '#ff0033', '#ff0033', '#ff0033',
           '#ff0033', '#ff6600', '#ff0033', '#ff0033', '#000000',
           '#ff0033', '#ff0033', '#000033', '#000033', '#ff6600',
           '#000000', '#000000', '#ff0033', '#000033', '#000033',
           '#ff0033', '#000000', '#000000', '#000000', '#ff0033',
           '#ff0033', '#ff0033', '#ff0033', '#ff0033', '#ff0033',
           '#000000', '#000000', '#000000', '#000000', '#000000',
           '#ff0033', '#ff0033', '#ff0033', '#ff0033', '#ff0033',
           '#000000', '#000000', '#000000', '#000000', '#ff0033',
           '#ff0033', '#000000', '#000000', '#000000', '#000000',
           '#000000', '#000000', '#000000', '#000000', '#000000',
           '#000000', '#ff0033', '#000000', '#000000', '#ff0033',
           '#000000', '#000000', '#000000', '#000000', '#000000',
           '#000000', '#ff6600', '#ff6600', '#ff6600', '#000000',
           '#000000', '#ff0033', '#ff6600', '#ff6600', '#000000',
           '#000000', '#000000', '#000000', '#000000', '#000000',
           '#000000', '#000000', '#000000', '#000000', '#ff6600',
           '#ff6600', '#ff0033', '#000000', '#000000', '#ff6600',
           '#ff6600', '#ff6600', '#ff0033', '#000000', '#000000',
           '#000000']

Qbert02 = ['#000000', '#000000', '#000000', '#000000', '#ff6600',
           '#ff6600', '#ff6600', '#ff6600', '#000000', '#000000',
           '#000000', '#000000', '#000000', '#000000', '#000000',
           '#000000', '#000000', '#000000', '#000000', '#000000',
           '#000000', '#000000', '#ff0033', '#ff0033', '#ff0033',
           '#ff0033', '#ff0033', '#ff6600', '#ff6600', '#ff6600',
           '#000000', '#000000', '#000000', '#ff0033', '#ff0033',
           '#ff6600', '#ff0033', '#ffffff', '#ffffff', '#ff0033',
           '#ffffff', '#ffffff', '#000000', '#000000', '#000000',
           '#000000', '#000000', '#000000', '#000000', '#000000',
           '#000000', '#000000', '#000000', '#000000', '#000000',
           '#000000', '#ff0033', '#000000', '#000000', '#ff0033',
           '#ff6600', '#ff6600', '#ff0033', '#000000', '#ff0033',
           '#ff0033', '#ff0033', '#ff6600', '#ff0033', '#000000',
           '#000000', '#ff0033', '#000000', '#000000', '#ff6600',
           '#000000', '#000000', '#000000', '#000000', '#000000',
           '#000000', '#000000', '#000000', '#ff6600', '#ff6600',
           '#ff6600', '#ff6600', '#ff6600', '#ff6600', '#ff0033',
           '#ff0033', '#ff6600', '#ff6600', '#ff6600', '#ff0033',
           '#ff0033', '#ff0033', '#ff0033', '#ff0033', '#ff6600',
           '#ff6600', '#ff6600', '#ff6600', '#ff6600', '#ff6600',
           '#ff6600', '#ff6600', '#ff6600', '#ff6600', '#ff6600',
           '#000000', '#000000', '#000000', '#ff6600', '#ff6600',
           '#ff6600', '#ff0033', '#ff0033', '#ff0033', '#ff6600',
           '#ff0033', '#ff6600', '#ff0033', '#ff6600', '#ff0033',
           '#ff6600', '#ff0033', '#ff0033', '#000000', '#ff0033',
           '#ff0033', '#ff0033', '#ff0033', '#ff0033', '#ff6600',
           '#ff0033', '#ff0033', '#000000', '#ff0033', '#ff0033',
           '#000000', '#000000', '#ff6600', '#000000', '#000000',
           '#ff0033', '#000000', '#000000', '#ff0033', '#000000',
           '#000000', '#000000', '#ff0033', '#ff0033', '#ff0033',
           '#ff0033', '#ff0033', '#ff0033', '#000000', '#000000',
           '#000000', '#000000', '#000000', '#ff0033', '#ff0033',
           '#ff0033', '#ff0033', '#ff0033', '#000000', '#000000',
           '#000000', '#000000', '#ff0033', '#ff0033', '#000000',
           '#000000', '#000000', '#000000', '#000000', '#000000',
           '#000000', '#000000', '#000000', '#000000', '#ff0033',
           '#000000', '#000000', '#000000', '#ff0033', '#000000',
           '#000000', '#000000', '#000000', '#000000', '#000000',
           '#ff0033', '#000000', '#000000', '#000000', '#ff0033',
           '#000000', '#000000', '#000000', '#000000', '#000000',
           '#000000', '#000000', '#000000', '#000000', '#000000',
           '#000000', '#000000', '#000000', '#000000', '#000000',
           '#000000', '#ff0033', '#000000', '#000000', '#000000',
           '#ff0033', '#000000', '#000000', '#000000', '#000000',
           '#000000', '#ff6600', '#ff6600', '#ff6600', '#000000',
           '#000000', '#ff0033', '#ff6600', '#ff6600', '#000000',
           '#000000', '#000000', '#000000', '#000000', '#000000',
           '#000000', '#000000', '#000000', '#000000', '#ff6600',
           '#ff6600', '#ff0033', '#000000', '#000000', '#ff6600',
           '#ff6600', '#ff6600', '#ff0033', '#000000', '#000000',
           '#000000']

BombJack01 = ['#333366', '#333366', '#333366', '#333366', '#333366',
              '#333366', '#333366', '#333366', '#333366', '#333366',
              '#333366', '#333366', '#333366', '#333366', '#333366',
              '#333366', '#333366', '#333366', '#333366', '#0099ff',
              '#333366', '#333366', '#0099ff', '#0099ff', '#0099ff',
              '#0099ff', '#0099ff', '#333366', '#333366', '#0099ff',
              '#333366', '#333366', '#333366', '#333366', '#0099ff',
              '#0099ff', '#0099ff', '#0099ff', '#0099ff', '#0099ff',
              '#0099ff', '#0099ff', '#0099ff', '#0099ff', '#0099ff',
              '#333366', '#333366', '#333366', '#333366', '#333366',
              '#333366', '#0099ff', '#0099ff', '#0099ff', '#ffffff',
              '#ffffff', '#0099ff', '#ffffff', '#ffffff', '#0099ff',
              '#0099ff', '#0099ff', '#333366', '#333366', '#333366',
              '#333366', '#333366', '#0099ff', '#0099ff', '#ffffff',
              '#000000', '#0099ff', '#000000', '#ffffff', '#0099ff',
              '#0099ff', '#333366', '#333366', '#333366', '#333366',
              '#333366', '#333366', '#333366', '#333366', '#333366',
              '#0099ff', '#ffffff', '#000000', '#0099ff', '#000000',
              '#ffffff', '#0099ff', '#333366', '#333366', '#333366',
              '#333366', '#333366', '#333366', '#333366', '#333366',
              '#333366', '#ffcc99', '#ffcc99', '#ffcc99', '#ffcc99',
              '#ffcc99', '#333366', '#333366', '#333366', '#333366',
              '#333366', '#333366', '#333366', '#333366', '#333366',
              '#333366', '#333366', '#ffffff', '#ffcc99', '#ffcc99',
              '#ffcc99', '#ffcc99', '#ffcc99', '#ffffff', '#333366',
              '#333366', '#333366', '#333366', '#333366', '#333366',
              '#333366', '#ff0000', '#ff0000', '#ffffff', '#ffffff',
              '#ffffff', '#ffffff', '#ffffff', '#ff0000', '#ff0000',
              '#333366', '#333366', '#333366', '#333366', '#333366',
              '#333366', '#333366', '#ff0000', '#ff0000', '#ff0000',
              '#ff0000', '#000000', '#ff0000', '#000000', '#ff0000',
              '#ff0000', '#ff0000', '#ff0000', '#333366', '#333366',
              '#333366', '#000000', '#000000', '#ff0000', '#ff0000',
              '#ff0000', '#ff0000', '#ff0000', '#ff0000', '#ff0000',
              '#ff0000', '#ff0000', '#000000', '#000000', '#333366',
              '#333366', '#333366', '#333366', '#000000', '#000000',
              '#ffffff', '#0099ff', '#0099ff', '#0099ff', '#ffff00',
              '#0099ff', '#0099ff', '#0099ff', '#ffffff', '#000000',
              '#000000', '#333366', '#333366', '#ffffff', '#ffffff',
              '#ffffff', '#ff0000', '#ff0000', '#ff0000', '#ff0000',
              '#ff0000', '#ff0000', '#ff0000', '#ffffff', '#ffffff',
              '#ffffff', '#333366', '#333366', '#333366', '#333366',
              '#ffffff', '#ffffff', '#ffffff', '#ff0000', '#ff0000',
              '#ff0000', '#ff0000', '#ff0000', '#ff0000', '#ff0000',
              '#ffffff', '#ffffff', '#ffffff', '#333366', '#333366',
              '#333366', '#ffffff', '#ffffff', '#ffffff', '#ff0000',
              '#ff0000', '#ffffff', '#ff0000', '#ff0000', '#ffffff',
              '#ffffff', '#ffffff', '#ffffff', '#333366', '#333366',
              '#333366', '#333366', '#333366', '#333366', '#333366',
              '#000000', '#000000', '#000000', '#333366', '#000000',
              '#000000', '#000000', '#333366', '#333366', '#333366',
              '#333366']

BombJack02 = ['#333366', '#333366', '#333366', '#333366', '#333366',
              '#333366', '#333366', '#333366', '#333366', '#333366',
              '#333366', '#333366', '#333366', '#333366', '#333366',
              '#333366', '#333366', '#333366', '#333366', '#0099ff',
              '#333366', '#333366', '#0099ff', '#0099ff', '#0099ff',
              '#0099ff', '#0099ff', '#333366', '#333366', '#0099ff',
              '#333366', '#333366', '#333366', '#333366', '#0099ff',
              '#0099ff', '#0099ff', '#0099ff', '#0099ff', '#0099ff',
              '#0099ff', '#0099ff', '#0099ff', '#0099ff', '#0099ff',
              '#333366', '#333366', '#333366', '#333366', '#333366',
              '#333366', '#0099ff', '#0099ff', '#0099ff', '#ffffff',
              '#000000', '#0099ff', '#000000', '#ffffff', '#0099ff',
              '#0099ff', '#0099ff', '#333366', '#333366', '#333366',
              '#333366', '#333366', '#0099ff', '#0099ff', '#ffffff',
              '#000000', '#0099ff', '#000000', '#ffffff', '#0099ff',
              '#0099ff', '#333366', '#333366', '#333366', '#333366',
              '#333366', '#333366', '#000000', '#000000', '#333366',
              '#0099ff', '#ffffff', '#ffffff', '#ffcc99', '#ffffff',
              '#ffffff', '#0099ff', '#333366', '#000000', '#000000',
              '#333366', '#333366', '#000000', '#000000', '#ff0000',
              '#ffcc99', '#000000', '#000000', '#000000', '#000000',
              '#000000', '#ffcc99', '#ff0000', '#000000', '#000000',
              '#333366', '#333366', '#333366', '#333366', '#333366',
              '#ff0000', '#ff0000', '#ffffff', '#ffcc99', '#ffcc99',
              '#ffcc99', '#ffcc99', '#ffcc99', '#ffffff', '#ff0000',
              '#ff0000', '#333366', '#333366', '#333366', '#333366',
              '#333366', '#ff0000', '#ff0000', '#ffffff', '#ffffff',
              '#ffffff', '#ffffff', '#ffffff', '#ff0000', '#ff0000',
              '#ffffff', '#333366', '#333366', '#333366', '#333366',
              '#333366', '#ffffff', '#ffffff', '#ffffff', '#ff0000',
              '#ff0000', '#000000', '#ff0000', '#000000', '#ff0000',
              '#ff0000', '#ffffff', '#ffffff', '#333366', '#333366',
              '#333366', '#333366', '#ffffff', '#ffffff', '#ff0000',
              '#ff0000', '#ff0000', '#ff0000', '#ff0000', '#ff0000',
              '#ff0000', '#ffffff', '#ffffff', '#ffffff', '#333366',
              '#333366', '#333366', '#333366', '#ffffff', '#ffffff',
              '#ffffff', '#0099ff', '#0099ff', '#0099ff', '#ffff00',
              '#0099ff', '#0099ff', '#0099ff', '#ffffff', '#ffffff',
              '#ffffff', '#333366', '#333366', '#ffffff', '#ffffff',
              '#ffffff', '#ff0000', '#ff0000', '#ff0000', '#ff0000',
              '#ff0000', '#ff0000', '#ff0000', '#ffffff', '#ffffff',
              '#ffffff', '#ffffff', '#333366', '#333366', '#ffffff',
              '#ffffff', '#ffffff', '#ffffff', '#ff0000', '#ff0000',
              '#ff0000', '#ff0000', '#ff0000', '#ff0000', '#ff0000',
              '#ffffff', '#ffffff', '#ffffff', '#ffffff', '#333366',
              '#333366', '#333366', '#ffffff', '#ffffff', '#ff0000',
              '#ff0000', '#ffffff', '#ff0000', '#ff0000', '#ffffff',
              '#333366', '#ffffff', '#ffffff', '#333366', '#333366',
              '#333366', '#333366', '#333366', '#333366', '#333366',
              '#000000', '#000000', '#000000', '#333366', '#000000',
              '#000000', '#000000', '#333366', '#333366', '#333366',
              '#333366']

Link01 = [ '#666666', '#666666', '#666666', '#666666', '#666666', '#666666', '#666666', '#66cc00', '#66cc00', '#66cc00', '#66cc00', '#666666', '#666666', '#666666', '#666666', '#666666', 
'#666666', '#666666', '#666666', '#66cc00', '#66cc00', '#66cc00', '#66cc00', '#66cc00', '#cc3300', '#cc3300', '#cc3300', '#cc3300', '#666666', '#666666', '#666666', '#666666', 
'#666666', '#666666', '#666666', '#cc3300', '#cc3300', '#cc3300', '#cc3300', '#cc3300', '#cc3300', '#66cc00', '#66cc00', '#ff9933', '#66cc00', '#66cc00', '#66cc00', '#666666', 
'#66cc00', '#66cc00', '#66cc00', '#66cc00', '#ff9933', '#ff9933', '#cc3300', '#cc3300', '#cc3300', '#cc3300', '#cc3300', '#cc3300', '#666666', '#666666', '#666666', '#666666', 
'#666666', '#cc3300', '#666666', '#666666', '#ff9933', '#66cc00', '#ff9933', '#ff9933', '#cc3300', '#ff9933', '#ff9933', '#ff9933', '#66cc00', '#66cc00', '#666666', '#66cc00', 
'#666666', '#666666', '#66cc00', '#cc3300', '#cc3300', '#ff9933', '#ff9933', '#cc3300', '#ff9933', '#ff9933', '#cc3300', '#ff9933', '#ff9933', '#ff9933', '#cc3300', '#666666', 
'#666666', '#cc3300', '#666666', '#666666', '#ff9933', '#ff9933', '#ff9933', '#ff9933', '#ff9933', '#ff9933', '#cc3300', '#cc3300', '#cc3300', '#666666', '#666666', '#666666', 
'#666666', '#666666', '#666666', '#666666', '#66cc00', '#66cc00', '#66cc00', '#66cc00', '#ff9933', '#ff9933', '#ff9933', '#ff9933', '#666666', '#666666', '#cc3300', '#666666', 
'#666666', '#cc3300', '#ff9933', '#cc3300', '#cc3300', '#cc3300', '#66cc00', '#66cc00', '#66cc00', '#66cc00', '#66cc00', '#66cc00', '#66cc00', '#cc3300', '#666666', '#666666', 
'#666666', '#cc3300', '#cc3300', '#cc3300', '#66cc00', '#ff9933', '#ff9933', '#ff9933', '#66cc00', '#66cc00', '#66cc00', '#cc3300', '#cc3300', '#ff9933', '#cc3300', '#666666', 
'#666666', '#cc3300', '#666666', '#cc3300', '#cc3300', '#66cc00', '#66cc00', '#66cc00', '#ff9933', '#ff9933', '#ff9933', '#cc3300', '#cc3300', '#cc3300', '#cc3300', '#666666', 
'#666666', '#cc3300', '#cc3300', '#cc3300', '#cc3300', '#ff9933', '#ff9933', '#66cc00', '#66cc00', '#66cc00', '#cc3300', '#666666', '#666666', '#666666', '#cc3300', '#666666', 
'#666666', '#cc3300', '#666666', '#666666', '#666666', '#cc3300', '#cc3300', '#cc3300', '#cc3300', '#66cc00', '#66cc00', '#cc3300', '#cc3300', '#66cc00', '#666666', '#666666', 
'#666666', '#66cc00', '#66cc00', '#66cc00', '#66cc00', '#66cc00', '#66cc00', '#66cc00', '#66cc00', '#66cc00', '#66cc00', '#666666', '#666666', '#666666', '#666666', '#666666', 
'#666666', '#666666', '#666666', '#666666', '#666666', '#666666', '#666666', '#666666', '#cc3300', '#cc3300', '#cc3300', '#cc3300', '#666666', '#666666', '#666666', '#666666', 
'#666666', '#666666', '#666666', '#666666', '#cc3300', '#cc3300', '#cc3300', '#cc3300', '#cc3300', '#666666', '#666666', '#666666', '#666666', '#666666', '#666666', '#666666']

Link02 = ['#666666', '#666666', '#666666', '#666666', '#666666', '#666666', '#666666', '#666666', '#666666', '#666666', '#666666', '#666666', '#666666', '#666666', '#666666', '#666666', 
'#666666', '#666666', '#666666', '#666666', '#666666', '#66cc00', '#66cc00', '#66cc00', '#66cc00', '#666666', '#666666', '#666666', '#666666', '#666666', '#666666', '#666666', 
'#666666', '#666666', '#666666', '#666666', '#cc3300', '#cc3300', '#cc3300', '#cc3300', '#66cc00', '#66cc00', '#66cc00', '#66cc00', '#66cc00', '#666666', '#666666', '#666666', 
'#666666', '#66cc00', '#66cc00', '#66cc00', '#ff9933', '#66cc00', '#66cc00', '#cc3300', '#cc3300', '#cc3300', '#cc3300', '#cc3300', '#cc3300', '#666666', '#666666', '#666666', 
'#666666', '#666666', '#666666', '#666666', '#cc3300', '#cc3300', '#cc3300', '#cc3300', '#cc3300', '#cc3300', '#ff9933', '#ff9933', '#66cc00', '#66cc00', '#66cc00', '#66cc00', 
'#66cc00', '#666666', '#66cc00', '#66cc00', '#ff9933', '#ff9933', '#ff9933', '#cc3300', '#ff9933', '#ff9933', '#66cc00', '#ff9933', '#666666', '#666666', '#666666', '#666666', 
'#666666', '#666666', '#ff9933', '#ff9933', '#ff9933', '#cc3300', '#ff9933', '#ff9933', '#cc3300', '#ff9933', '#ff9933', '#cc3300', '#cc3300', '#66cc00', '#666666', '#666666', 
'#666666', '#666666', '#666666', '#cc3300', '#cc3300', '#cc3300', '#ff9933', '#ff9933', '#ff9933', '#ff9933', '#ff9933', '#ff9933', '#666666', '#cc3300', '#666666', '#666666', 
'#666666', '#666666', '#cc3300', '#666666', '#ff9933', '#ff9933', '#ff9933', '#ff9933', '#66cc00', '#66cc00', '#66cc00', '#66cc00', '#666666', '#666666', '#666666', '#666666', 
'#666666', '#666666', '#66cc00', '#cc3300', '#cc3300', '#66cc00', '#66cc00', '#ff9933', '#ff9933', '#ff9933', '#cc3300', '#cc3300', '#ff9933', '#cc3300', '#666666', '#666666', 
'#666666', '#666666', '#cc3300', '#ff9933', '#cc3300', '#66cc00', '#ff9933', '#ff9933', '#ff9933', '#cc3300', '#cc3300', '#cc3300', '#cc3300', '#cc3300', '#666666', '#666666', 
'#666666', '#66cc00', '#cc3300', '#cc3300', '#cc3300', '#cc3300', '#cc3300', '#ff9933', '#ff9933', '#66cc00', '#66cc00', '#cc3300', '#666666', '#cc3300', '#666666', '#666666', 
'#666666', '#666666', '#cc3300', '#666666', '#666666', '#cc3300', '#66cc00', '#66cc00', '#66cc00', '#cc3300', '#cc3300', '#cc3300', '#cc3300', '#66cc00', '#66cc00', '#666666', 
'#cc3300', '#cc3300', '#66cc00', '#66cc00', '#66cc00', '#66cc00', '#66cc00', '#cc3300', '#cc3300', '#cc3300', '#cc3300', '#66cc00', '#666666', '#cc3300', '#666666', '#666666', 
'#666666', '#666666', '#666666', '#cc3300', '#cc3300', '#66cc00', '#66cc00', '#66cc00', '#66cc00', '#66cc00', '#66cc00', '#66cc00', '#66cc00', '#cc3300', '#cc3300', '#cc3300', 
'#666666', '#cc3300', '#cc3300', '#cc3300', '#666666', '#666666', '#666666', '#666666', '#666666', '#cc3300', '#cc3300', '#cc3300', '#666666', '#666666', '#666666', '#666666']

Mario01 = ['#000000', '#000000', '#000000', '#000000', '#000000', '#000000', '#000000', '#000000', '#000000', '#000000', '#000000', '#000000', '#000000', '#000000', '#000000', '#000000', 
'#000000', '#000000', '#000000', '#000000', '#000000', '#b13425', '#b13425', '#b13425', '#b13425', '#b13425', '#000000', '#000000', '#000000', '#000000', '#000000', '#000000', 
'#000000', '#000000', '#000000', '#b13425', '#b13425', '#b13425', '#b13425', '#b13425', '#b13425', '#b13425', '#b13425', '#b13425', '#000000', '#000000', '#000000', '#000000', 
'#000000', '#000000', '#000000', '#000000', '#6a6b04', '#6a6b04', '#6a6b04', '#e39d25', '#e39d25', '#6a6b04', '#e39d25', '#000000', '#000000', '#000000', '#000000', '#000000', 
'#000000', '#000000', '#000000', '#e39d25', '#e39d25', '#e39d25', '#6a6b04', '#e39d25', '#e39d25', '#e39d25', '#6a6b04', '#e39d25', '#6a6b04', '#000000', '#000000', '#000000', 
'#000000', '#000000', '#000000', '#6a6b04', '#e39d25', '#6a6b04', '#6a6b04', '#e39d25', '#e39d25', '#e39d25', '#6a6b04', '#e39d25', '#e39d25', '#e39d25', '#000000', '#000000', 
'#000000', '#000000', '#000000', '#6a6b04', '#6a6b04', '#6a6b04', '#6a6b04', '#e39d25', '#e39d25', '#e39d25', '#e39d25', '#6a6b04', '#6a6b04', '#000000', '#000000', '#000000', 
'#000000', '#000000', '#000000', '#000000', '#000000', '#e39d25', '#e39d25', '#e39d25', '#e39d25', '#e39d25', '#e39d25', '#e39d25', '#000000', '#000000', '#000000', '#000000', 
'#000000', '#000000', '#000000', '#000000', '#e39d25', '#000000', '#6a6b04', '#b13425', '#6a6b04', '#6a6b04', '#6a6b04', '#6a6b04', '#000000', '#000000', '#000000', '#000000', 
'#000000', '#000000', '#000000', '#e39d25', '#6a6b04', '#6a6b04', '#6a6b04', '#6a6b04', '#6a6b04', '#6a6b04', '#e39d25', '#e39d25', '#e39d25', '#000000', '#000000', '#000000', 
'#000000', '#000000', '#000000', '#000000', '#e39d25', '#e39d25', '#6a6b04', '#6a6b04', '#6a6b04', '#6a6b04', '#6a6b04', '#b13425', '#e39d25', '#e39d25', '#000000', '#000000', 
'#000000', '#000000', '#6a6b04', '#6a6b04', '#b13425', '#b13425', '#b13425', '#b13425', '#b13425', '#b13425', '#b13425', '#000000', '#000000', '#000000', '#000000', '#000000', 
'#000000', '#000000', '#000000', '#000000', '#000000', '#b13425', '#b13425', '#b13425', '#b13425', '#b13425', '#b13425', '#b13425', '#b13425', '#6a6b04', '#000000', '#000000', 
'#000000', '#6a6b04', '#6a6b04', '#b13425', '#b13425', '#b13425', '#000000', '#b13425', '#b13425', '#b13425', '#000000', '#000000', '#000000', '#000000', '#000000', '#000000', 
'#000000', '#000000', '#000000', '#000000', '#000000', '#000000', '#000000', '#6a6b04', '#6a6b04', '#6a6b04', '#000000', '#000000', '#000000', '#000000', '#6a6b04', '#000000', 
'#000000', '#000000', '#000000', '#000000', '#000000', '#000000', '#6a6b04', '#6a6b04', '#6a6b04', '#6a6b04', '#000000', '#000000', '#000000', '#000000', '#000000', '#000000']

Mario02 = ['#000000', '#000000', '#000000', '#000000', '#000000', '#000000', '#b13425', '#b13425', '#b13425', '#b13425', '#b13425', '#000000', '#000000', '#000000', '#000000', '#000000', 
'#000000', '#000000', '#000000', '#000000', '#b13425', '#b13425', '#b13425', '#b13425', '#b13425', '#b13425', '#b13425', '#b13425', '#b13425', '#000000', '#000000', '#000000', 
'#000000', '#000000', '#000000', '#000000', '#000000', '#e39d25', '#6a6b04', '#e39d25', '#e39d25', '#6a6b04', '#6a6b04', '#6a6b04', '#000000', '#000000', '#000000', '#000000', 
'#000000', '#000000', '#000000', '#6a6b04', '#e39d25', '#6a6b04', '#e39d25', '#e39d25', '#e39d25', '#6a6b04', '#e39d25', '#e39d25', '#e39d25', '#000000', '#000000', '#000000', 
'#000000', '#000000', '#e39d25', '#e39d25', '#e39d25', '#6a6b04', '#e39d25', '#e39d25', '#e39d25', '#6a6b04', '#6a6b04', '#e39d25', '#6a6b04', '#000000', '#000000', '#000000', 
'#000000', '#000000', '#000000', '#6a6b04', '#6a6b04', '#e39d25', '#e39d25', '#e39d25', '#e39d25', '#6a6b04', '#6a6b04', '#6a6b04', '#6a6b04', '#000000', '#000000', '#000000', 
'#000000', '#000000', '#000000', '#000000', '#e39d25', '#e39d25', '#e39d25', '#e39d25', '#e39d25', '#e39d25', '#e39d25', '#000000', '#000000', '#000000', '#000000', '#000000', 
'#000000', '#000000', '#000000', '#000000', '#6a6b04', '#6a6b04', '#b13425', '#6a6b04', '#6a6b04', '#6a6b04', '#000000', '#000000', '#000000', '#000000', '#000000', '#000000', 
'#000000', '#000000', '#000000', '#000000', '#000000', '#6a6b04', '#6a6b04', '#b13425', '#b13425', '#6a6b04', '#6a6b04', '#6a6b04', '#6a6b04', '#000000', '#000000', '#000000', 
'#000000', '#000000', '#000000', '#6a6b04', '#6a6b04', '#6a6b04', '#b13425', '#b13425', '#e39d25', '#b13425', '#b13425', '#e39d25', '#000000', '#000000', '#000000', '#000000', 
'#000000', '#000000', '#000000', '#000000', '#b13425', '#b13425', '#b13425', '#b13425', '#b13425', '#6a6b04', '#6a6b04', '#6a6b04', '#6a6b04', '#000000', '#000000', '#000000', 
'#000000', '#000000', '#000000', '#b13425', '#6a6b04', '#6a6b04', '#e39d25', '#e39d25', '#e39d25', '#b13425', '#b13425', '#b13425', '#000000', '#000000', '#000000', '#000000', 
'#000000', '#000000', '#000000', '#000000', '#000000', '#b13425', '#b13425', '#b13425', '#e39d25', '#e39d25', '#6a6b04', '#b13425', '#000000', '#000000', '#000000', '#000000', 
'#000000', '#000000', '#000000', '#000000', '#000000', '#b13425', '#b13425', '#b13425', '#6a6b04', '#6a6b04', '#6a6b04', '#000000', '#000000', '#000000', '#000000', '#000000', 
'#000000', '#000000', '#000000', '#000000', '#6a6b04', '#6a6b04', '#6a6b04', '#6a6b04', '#6a6b04', '#6a6b04', '#6a6b04', '#000000', '#000000', '#000000', '#000000', '#000000', 
'#000000', '#000000', '#000000', '#000000', '#000000', '#6a6b04', '#6a6b04', '#6a6b04', '#6a6b04', '#000000', '#000000', '#000000', '#000000', '#000000', '#000000', '#000000']

Mario03 = ['#000000', '#000000', '#000000', '#000000', '#000000', '#000000', '#b13425', '#b13425', '#b13425', '#b13425', '#b13425', '#000000', '#000000', '#000000', '#000000', '#000000', 
'#000000', '#000000', '#000000', '#000000', '#b13425', '#b13425', '#b13425', '#b13425', '#b13425', '#b13425', '#b13425', '#b13425', '#b13425', '#000000', '#000000', '#000000', 
'#000000', '#000000', '#000000', '#000000', '#000000', '#e39d25', '#6a6b04', '#e39d25', '#e39d25', '#6a6b04', '#6a6b04', '#6a6b04', '#000000', '#000000', '#000000', '#000000', 
'#000000', '#000000', '#000000', '#6a6b04', '#e39d25', '#6a6b04', '#e39d25', '#e39d25', '#e39d25', '#6a6b04', '#e39d25', '#e39d25', '#e39d25', '#000000', '#000000', '#000000', 
'#000000', '#000000', '#e39d25', '#e39d25', '#e39d25', '#6a6b04', '#e39d25', '#e39d25', '#e39d25', '#6a6b04', '#6a6b04', '#e39d25', '#6a6b04', '#000000', '#000000', '#000000', 
'#000000', '#000000', '#000000', '#6a6b04', '#6a6b04', '#e39d25', '#e39d25', '#e39d25', '#e39d25', '#6a6b04', '#6a6b04', '#6a6b04', '#6a6b04', '#000000', '#000000', '#000000', 
'#000000', '#000000', '#000000', '#000000', '#e39d25', '#e39d25', '#e39d25', '#e39d25', '#e39d25', '#e39d25', '#e39d25', '#000000', '#000000', '#000000', '#000000', '#000000', 
'#000000', '#000000', '#6a6b04', '#6a6b04', '#6a6b04', '#6a6b04', '#b13425', '#b13425', '#6a6b04', '#6a6b04', '#000000', '#000000', '#000000', '#000000', '#000000', '#000000', 
'#000000', '#e39d25', '#e39d25', '#e39d25', '#6a6b04', '#6a6b04', '#6a6b04', '#b13425', '#b13425', '#b13425', '#6a6b04', '#6a6b04', '#6a6b04', '#6a6b04', '#e39d25', '#e39d25', 
'#e39d25', '#e39d25', '#e39d25', '#000000', '#6a6b04', '#6a6b04', '#b13425', '#e39d25', '#b13425', '#b13425', '#b13425', '#6a6b04', '#6a6b04', '#e39d25', '#e39d25', '#000000', 
'#000000', '#000000', '#6a6b04', '#000000', '#000000', '#b13425', '#b13425', '#b13425', '#b13425', '#b13425', '#b13425', '#b13425', '#000000', '#000000', '#e39d25', '#e39d25', 
'#000000', '#000000', '#000000', '#b13425', '#b13425', '#b13425', '#b13425', '#b13425', '#b13425', '#b13425', '#b13425', '#b13425', '#6a6b04', '#6a6b04', '#000000', '#000000', 
'#000000', '#000000', '#6a6b04', '#6a6b04', '#b13425', '#b13425', '#b13425', '#b13425', '#b13425', '#b13425', '#b13425', '#b13425', '#b13425', '#b13425', '#000000', '#000000', 
'#000000', '#6a6b04', '#6a6b04', '#b13425', '#b13425', '#b13425', '#000000', '#000000', '#000000', '#b13425', '#b13425', '#b13425', '#6a6b04', '#6a6b04', '#000000', '#000000', 
'#000000', '#000000', '#000000', '#000000', '#000000', '#000000', '#000000', '#000000', '#000000', '#000000', '#000000', '#000000', '#6a6b04', '#6a6b04', '#6a6b04', '#000000', 
'#000000', '#000000', '#6a6b04', '#6a6b04', '#6a6b04', '#000000', '#000000', '#000000', '#000000', '#000000', '#000000', '#000000', '#000000', '#000000', '#000000', '#000000']

# Concatenate arrays into a single list
DigDug = [DigDug01, DigDug02]
Qbert = [Qbert01, Qbert02]
BombJack = [BombJack01, BombJack02]
Link = [Link01, Link02]
Mario = [Mario01, Mario02, Mario03]

# Convert to RGB values
def convert_to_rgb(hx):
    if re.compile(r'#[a-fA-F0-9]{3}').match(hx):
        div = 0
        return tuple(int(hx[i:i + 2], 16) / div if div else
                     int(hx[i:i + 2], 16) for i in (1, 3, 5))
    else:
        raise ValueError(f'"{hx}" <-- wtf is that?')


# Call with game and desired frame, return frame data array

def play(game, frame):
    origdata = game[frame]
    framedata = []
    for i in range(256):
        framedata.append(convert_to_rgb(origdata[i]))
    return framedata


