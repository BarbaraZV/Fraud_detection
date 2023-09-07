{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0036ea6e",
   "metadata": {},
   "outputs": [],
   "source": [
    "#python datagen.py -n <NUMBER_OF_CUSTOMERS_TO_GENERATE> -o <OUTPUT_FOLDER> <START_DATE> <END_DATE>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "ead002c6",
   "metadata": {},
   "outputs": [
    {
     "ename": "ModuleNotFoundError",
     "evalue": "No module named 'datagen_customer'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mModuleNotFoundError\u001b[0m                       Traceback (most recent call last)",
      "Input \u001b[1;32mIn [1]\u001b[0m, in \u001b[0;36m<cell line: 7>\u001b[1;34m()\u001b[0m\n\u001b[0;32m      4\u001b[0m \u001b[38;5;28;01mimport\u001b[39;00m \u001b[38;5;21;01mjson\u001b[39;00m\n\u001b[0;32m      5\u001b[0m \u001b[38;5;28;01mfrom\u001b[39;00m \u001b[38;5;21;01mmultiprocessing\u001b[39;00m \u001b[38;5;28;01mimport\u001b[39;00m Pool, cpu_count\n\u001b[1;32m----> 7\u001b[0m \u001b[38;5;28;01mfrom\u001b[39;00m \u001b[38;5;21;01mdatagen_customer\u001b[39;00m \u001b[38;5;28;01mimport\u001b[39;00m main \u001b[38;5;28;01mas\u001b[39;00m datagen_customers\n\u001b[0;32m      8\u001b[0m \u001b[38;5;28;01mfrom\u001b[39;00m \u001b[38;5;21;01mdatagen_transaction\u001b[39;00m \u001b[38;5;28;01mimport\u001b[39;00m main \u001b[38;5;28;01mas\u001b[39;00m datagen_transactions\n\u001b[0;32m      9\u001b[0m \u001b[38;5;28;01mfrom\u001b[39;00m \u001b[38;5;21;01mdatagen_transaction\u001b[39;00m \u001b[38;5;28;01mimport\u001b[39;00m valid_date\n",
      "\u001b[1;31mModuleNotFoundError\u001b[0m: No module named 'datagen_customer'"
     ]
    }
   ],
   "source": [
    "import argparse\n",
    "import pathlib\n",
    "import os\n",
    "import json\n",
    "from multiprocessing import Pool, cpu_count\n",
    "\n",
    "from datagen_customer import main as datagen_customers\n",
    "from datagen_transaction import main as datagen_transactions\n",
    "from datagen_transaction import valid_date\n",
    "\n",
    "\n",
    "if __name__ == '__main__':\n",
    "    parser = argparse.ArgumentParser(description='Customer Generator')\n",
    "    parser.add_argument('-n', '--nb_customers', type=int, help='Number of customers to generate', default=10)\n",
    "    parser.add_argument('start_date', type=valid_date, help='Transactions start date')\n",
    "    parser.add_argument('end_date', type=valid_date, help='Transactions start date')\n",
    "    parser.add_argument('-seed', type=int, nargs='?', help='Random generator seed', default=42)\n",
    "    parser.add_argument('-config', type=pathlib.Path, nargs='?', help='Profile config file (typically profiles/main_config.json\")', default='./profiles/main_config.json')\n",
    "    parser.add_argument('-c', '--customer_file', type=pathlib.Path, help='Customer file generated with the datagen_customer script', default=None)\n",
    "    parser.add_argument('-o', '--output', type=pathlib.Path, help='Output Folder path', default='data')\n",
    "\n",
    "\n",
    "    args = parser.parse_args()\n",
    "    num_cust = args.nb_customers\n",
    "    seed_num = args.seed\n",
    "    config = args.config\n",
    "    out_path = args.output\n",
    "    customer_file = args.customer_file\n",
    "    start_date = args.start_date\n",
    "    end_date = args.end_date\n",
    "    out_path = args.output\n",
    "    customers_out_file = customer_file or os.path.join(out_path, 'customers.csv')\n",
    "\n",
    "    # create the folder if it does not exist\n",
    "    if not os.path.exists(out_path):\n",
    "        os.makedirs(out_path)\n",
    "\n",
    "    # if no customers file provided, generate a customers file\n",
    "    if customer_file is None and num_cust is not None:\n",
    "        if os.path.exists(customers_out_file):\n",
    "            # prompt user to overwrite\n",
    "            agree = input(f\"File {customers_out_file} already exists. Overwrite? (y/N)\")\n",
    "            if agree.lower() != 'y':\n",
    "                exit(1)\n",
    "        datagen_customers(num_cust, seed_num, config, customers_out_file)\n",
    "    elif customer_file is None:\n",
    "        print('Either a customer file or a number of customers to create must be provided')\n",
    "        exit(1)\n",
    "    \n",
    "    # if we're supplied with a customer file, we need to figure how many we have\n",
    "    if customer_file is not None:\n",
    "        num_cust = 0\n",
    "        with open(customer_file, 'r') as f:\n",
    "            for row in f.readlines():\n",
    "                num_cust += 1\n",
    "\n",
    "    # figure out reasonable chunk size\n",
    "    num_cpu = cpu_count()\n",
    "    print(f\"Num CPUs: {num_cpu}\")\n",
    "    chunk_size = max(min(int(num_cust / 5), 1000), 1000 * int(num_cust / (1000 * num_cpu)))\n",
    "    # because from one profile to another, there may be a 10-50x difference in size, it is best to use small\n",
    "    # chunk sizes so as to spread the work across all CPUs. Bigger chunks means a core may process small profiles \n",
    "    # quickly and then be idle, while other cores process large profiles. Smaller chunks will run faster\n",
    "    \n",
    "    # zero padding determination\n",
    "    zero_pad = len(str(num_cust - 1))\n",
    "\n",
    "    # read config\n",
    "    with open(config, 'r') as f:\n",
    "        configs = json.load(f)\n",
    "\n",
    "    profile_names = configs.keys()\n",
    "\n",
    "    args_array = []\n",
    "    for profile_file in configs.keys():\n",
    "        customer_file_offset_start = 0\n",
    "        customer_file_offset_end = min(num_cust - 1, chunk_size - 1)\n",
    "        while customer_file_offset_start <= max(num_cust - 1, chunk_size):\n",
    "            print(f\"profile: {profile_file}, chunk size: {chunk_size}, \\\n",
    "                chunk: {customer_file_offset_start}-{customer_file_offset_end}\")\n",
    "            transactions_filename = os.path.join(out_path, \n",
    "                profile_file.replace('.json', \n",
    "                    f'_{str(customer_file_offset_start).zfill(zero_pad)}-{str(customer_file_offset_end).zfill(zero_pad)}.csv'))\n",
    "            # Arguments need to be passed as a tuple\n",
    "            args_array.append((\n",
    "                customers_out_file, \n",
    "                pathlib.Path(os.path.join('profiles', profile_file)), \n",
    "                start_date, \n",
    "                end_date, \n",
    "                transactions_filename,\n",
    "                customer_file_offset_start,\n",
    "                customer_file_offset_end\n",
    "            ))\n",
    "            customer_file_offset_start += chunk_size\n",
    "            customer_file_offset_end = min(num_cust - 1, customer_file_offset_end + chunk_size)\n",
    "\n",
    "    with Pool() as p:\n",
    "        p.starmap(datagen_transactions, args_array)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "fc487599",
   "metadata": {},
   "outputs": [],
   "source": []
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
