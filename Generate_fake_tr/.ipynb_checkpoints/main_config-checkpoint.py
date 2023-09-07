{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7d9291b3",
   "metadata": {},
   "outputs": [],
   "source": [
    "import json\n",
    "\n",
    "\n",
    "class MainConfig:\n",
    "\n",
    "    def __init__(self, main):\n",
    "        self.config = self.all_profiles_dicts(main)\n",
    "\n",
    "    # convert type to a tuple\n",
    "    def convert_config_type(self, x):\n",
    "        if type(x) is dict:\n",
    "            minval = float(x['min'])\n",
    "            maxval = float(x['max'])\n",
    "            if maxval < 0:\n",
    "                return (minval, float('inf'))\n",
    "            else:\n",
    "                return (minval, maxval)\n",
    "        else:\n",
    "            return x\n",
    "\n",
    "    def all_profiles_dicts(self, config):\n",
    "        with open(config, 'r') as f:\n",
    "            main_config = json.load(f)\n",
    "            all_profiles = {}\n",
    "            for pf in main_config:\n",
    "                if pf != 'leftovers.json':\n",
    "                    all_profiles[pf] = {}\n",
    "                    for qual in main_config[pf]:\n",
    "                        all_profiles[pf][qual] = \\\n",
    "                        self.convert_config_type(main_config[pf][qual])\n",
    "            return all_profiles"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.12"
  },
  "nbTranslate": {
   "displayLangs": [
    "*"
   ],
   "hotkey": "alt-t",
   "langInMainMenu": true,
   "sourceLang": "en",
   "targetLang": "fr",
   "useGoogleTranslate": true
  },
  "toc": {
   "base_numbering": 1,
   "nav_menu": {},
   "number_sections": true,
   "sideBar": true,
   "skip_h1_title": false,
   "title_cell": "Table of Contents",
   "title_sidebar": "Contents",
   "toc_cell": false,
   "toc_position": {},
   "toc_section_display": true,
   "toc_window_display": false
  },
  "varInspector": {
   "cols": {
    "lenName": 16,
    "lenType": 16,
    "lenVar": 40
   },
   "kernels_config": {
    "python": {
     "delete_cmd_postfix": "",
     "delete_cmd_prefix": "del ",
     "library": "var_list.py",
     "varRefreshCmd": "print(var_dic_list())"
    },
    "r": {
     "delete_cmd_postfix": ") ",
     "delete_cmd_prefix": "rm(",
     "library": "var_list.r",
     "varRefreshCmd": "cat(var_dic_list()) "
    }
   },
   "types_to_exclude": [
    "module",
    "function",
    "builtin_function_or_method",
    "instance",
    "_Feature"
   ],
   "window_display": false
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
