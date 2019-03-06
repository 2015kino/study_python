{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import math\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "8.0"
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import math\n",
    "math.pow(2,3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "28"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import random\n",
    "random.randint(0,100)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "ename": "ModuleNotFoundError",
     "evalue": "No module named 'atasisibs'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mModuleNotFoundError\u001b[0m                       Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-4-021ee51fd1a4>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m()\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[1;32mimport\u001b[0m \u001b[0matasisibs\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      2\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      3\u001b[0m \u001b[1;31m#mean\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      4\u001b[0m \u001b[0mname\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;36m1\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;36m5\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;36m12\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;36m46\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;36m33\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;36m21\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      5\u001b[0m \u001b[0mstatistics\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mmed\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mnuma\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mModuleNotFoundError\u001b[0m: No module named 'atasisibs'"
     ]
    }
   ],
   "source": [
    "import atasisibs\n",
    "\n",
    "#mean\n",
    "name=[1,5,12,46,33,21]\n",
    "statistics.med(numa)\n",
    "\n",
    "#median\n",
    "statistics.med(numa)\n",
    "\n",
    "#mode\n",
    "statistics.mods(numa)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "ename": "AttributeError",
     "evalue": "module 'statistics' has no attribute 'med'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mAttributeError\u001b[0m                            Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-5-a4a81a4df418>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m()\u001b[0m\n\u001b[0;32m      3\u001b[0m \u001b[1;31m#mean\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      4\u001b[0m \u001b[0mname\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;36m1\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;36m5\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;36m12\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;36m46\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;36m33\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;36m21\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 5\u001b[1;33m \u001b[0mstatistics\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mmed\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mnuma\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      6\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      7\u001b[0m \u001b[1;31m#median\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mAttributeError\u001b[0m: module 'statistics' has no attribute 'med'"
     ]
    }
   ],
   "source": [
    "import statistics\n",
    "\n",
    "#mean\n",
    "name=[1,5,12,46,33,21]\n",
    "statistics.med(numa)\n",
    "\n",
    "#median\n",
    "statistics.med(numa)\n",
    "\n",
    "#mode\n",
    "statistics.mods(numa)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "ename": "AttributeError",
     "evalue": "module 'statistics' has no attribute 'med'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mAttributeError\u001b[0m                            Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-6-a4a81a4df418>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m()\u001b[0m\n\u001b[0;32m      3\u001b[0m \u001b[1;31m#mean\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      4\u001b[0m \u001b[0mname\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;36m1\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;36m5\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;36m12\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;36m46\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;36m33\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;36m21\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 5\u001b[1;33m \u001b[0mstatistics\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mmed\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mnuma\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      6\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      7\u001b[0m \u001b[1;31m#median\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mAttributeError\u001b[0m: module 'statistics' has no attribute 'med'"
     ]
    }
   ],
   "source": [
    "import statistics\n",
    "\n",
    "#mean\n",
    "name=[1,5,12,46,33,21]\n",
    "statistics.med(numa)\n",
    "\n",
    "#median\n",
    "statistics.med(numa)\n",
    "\n",
    "#mode\n",
    "statistics.mods(numa)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "ename": "AttributeError",
     "evalue": "module 'statistics' has no attribute 'med'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mAttributeError\u001b[0m                            Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-7-e9b002467ece>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m()\u001b[0m\n\u001b[0;32m      3\u001b[0m \u001b[1;31m#mean\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      4\u001b[0m \u001b[0mname\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;36m1\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;36m5\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;36m12\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;36m46\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;36m33\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;36m21\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 5\u001b[1;33m \u001b[0mstatistics\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mmed\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mnuma\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      6\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      7\u001b[0m \u001b[1;31m#median\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mAttributeError\u001b[0m: module 'statistics' has no attribute 'med'"
     ]
    }
   ],
   "source": [
    "import statistics\n",
    "\n",
    "#mean\n",
    "name=[1,5,12,46,33,21]\n",
    "statistics.med(numa)\n",
    "\n",
    "#median\n",
    "statistics.median(numa)\n",
    "\n",
    "#mode\n",
    "statistics.mods(numa)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "ename": "AttributeError",
     "evalue": "module 'statistics' has no attribute 'med'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mAttributeError\u001b[0m                            Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-8-7943c1deb1ed>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m()\u001b[0m\n\u001b[0;32m      3\u001b[0m \u001b[1;31m#mean\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      4\u001b[0m \u001b[0mnume\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;36m1\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;36m5\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;36m12\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;36m46\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;36m33\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;36m21\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 5\u001b[1;33m \u001b[0mstatistics\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mmed\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mnuma\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      6\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      7\u001b[0m \u001b[1;31m#median\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mAttributeError\u001b[0m: module 'statistics' has no attribute 'med'"
     ]
    }
   ],
   "source": [
    "import statistics\n",
    "\n",
    "#mean\n",
    "nume=[1,5,12,46,33,21]\n",
    "statistics.med(numa)\n",
    "\n",
    "#median\n",
    "statistics.median(numa)\n",
    "\n",
    "#mode\n",
    "statistics.mods(numa)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "ename": "AttributeError",
     "evalue": "module 'statistics' has no attribute 'med'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mAttributeError\u001b[0m                            Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-9-7943c1deb1ed>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m()\u001b[0m\n\u001b[0;32m      3\u001b[0m \u001b[1;31m#mean\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      4\u001b[0m \u001b[0mnume\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;36m1\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;36m5\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;36m12\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;36m46\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;36m33\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;36m21\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 5\u001b[1;33m \u001b[0mstatistics\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mmed\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mnuma\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      6\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      7\u001b[0m \u001b[1;31m#median\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mAttributeError\u001b[0m: module 'statistics' has no attribute 'med'"
     ]
    }
   ],
   "source": [
    "import statistics\n",
    "\n",
    "#mean\n",
    "nume=[1,5,12,46,33,21]\n",
    "statistics.med(numa)\n",
    "\n",
    "#median\n",
    "statistics.median(numa)\n",
    "\n",
    "#mode\n",
    "statistics.mods(numa)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "ename": "StatisticsError",
     "evalue": "no unique mode; found 6 equally common values",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mStatisticsError\u001b[0m                           Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-10-61ea5bcbc480>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m()\u001b[0m\n\u001b[0;32m      9\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     10\u001b[0m \u001b[1;31m#mode\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m---> 11\u001b[1;33m \u001b[0mstatistics\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mmode\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mnume\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;32mD:\\anaconda\\lib\\statistics.py\u001b[0m in \u001b[0;36mmode\u001b[1;34m(data)\u001b[0m\n\u001b[0;32m    504\u001b[0m     \u001b[1;32melif\u001b[0m \u001b[0mtable\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    505\u001b[0m         raise StatisticsError(\n\u001b[1;32m--> 506\u001b[1;33m                 \u001b[1;34m'no unique mode; found %d equally common values'\u001b[0m \u001b[1;33m%\u001b[0m \u001b[0mlen\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mtable\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    507\u001b[0m                 )\n\u001b[0;32m    508\u001b[0m     \u001b[1;32melse\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mStatisticsError\u001b[0m: no unique mode; found 6 equally common values"
     ]
    }
   ],
   "source": [
    "import statistics\n",
    "\n",
    "#mean\n",
    "nume=[1,5,12,46,33,21]\n",
    "statistics.mean(nume)\n",
    "\n",
    "#median\n",
    "statistics.median(nume)\n",
    "\n",
    "#mode\n",
    "statistics.mode(nume)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "19.666666666666668"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import statistics\n",
    "\n",
    "#mean\n",
    "nume=[1,5,12,33,46,33,21]\n",
    "statistics.mean(nume)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "16.5"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#median\n",
    "statistics.median(nume)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "ename": "StatisticsError",
     "evalue": "no unique mode; found 6 equally common values",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mStatisticsError\u001b[0m                           Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-14-510e6c8cc9b4>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m()\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[1;31m#mode\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 2\u001b[1;33m \u001b[0mstatistics\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mmode\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mnume\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;32mD:\\anaconda\\lib\\statistics.py\u001b[0m in \u001b[0;36mmode\u001b[1;34m(data)\u001b[0m\n\u001b[0;32m    504\u001b[0m     \u001b[1;32melif\u001b[0m \u001b[0mtable\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    505\u001b[0m         raise StatisticsError(\n\u001b[1;32m--> 506\u001b[1;33m                 \u001b[1;34m'no unique mode; found %d equally common values'\u001b[0m \u001b[1;33m%\u001b[0m \u001b[0mlen\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mtable\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    507\u001b[0m                 )\n\u001b[0;32m    508\u001b[0m     \u001b[1;32melse\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mStatisticsError\u001b[0m: no unique mode; found 6 equally common values"
     ]
    }
   ],
   "source": [
    "#mode\n",
    "statistics.mode(nume)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "ename": "StatisticsError",
     "evalue": "no unique mode; found 6 equally common values",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mStatisticsError\u001b[0m                           Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-15-510e6c8cc9b4>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m()\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[1;31m#mode\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 2\u001b[1;33m \u001b[0mstatistics\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mmode\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mnume\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;32mD:\\anaconda\\lib\\statistics.py\u001b[0m in \u001b[0;36mmode\u001b[1;34m(data)\u001b[0m\n\u001b[0;32m    504\u001b[0m     \u001b[1;32melif\u001b[0m \u001b[0mtable\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    505\u001b[0m         raise StatisticsError(\n\u001b[1;32m--> 506\u001b[1;33m                 \u001b[1;34m'no unique mode; found %d equally common values'\u001b[0m \u001b[1;33m%\u001b[0m \u001b[0mlen\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mtable\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    507\u001b[0m                 )\n\u001b[0;32m    508\u001b[0m     \u001b[1;32melse\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mStatisticsError\u001b[0m: no unique mode; found 6 equally common values"
     ]
    }
   ],
   "source": [
    "#mode\n",
    "statistics.mode(nume)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "ename": "StatisticsError",
     "evalue": "no unique mode; found 6 equally common values",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mStatisticsError\u001b[0m                           Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-17-510e6c8cc9b4>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m()\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[1;31m#mode\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 2\u001b[1;33m \u001b[0mstatistics\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mmode\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mnume\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;32mD:\\anaconda\\lib\\statistics.py\u001b[0m in \u001b[0;36mmode\u001b[1;34m(data)\u001b[0m\n\u001b[0;32m    504\u001b[0m     \u001b[1;32melif\u001b[0m \u001b[0mtable\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    505\u001b[0m         raise StatisticsError(\n\u001b[1;32m--> 506\u001b[1;33m                 \u001b[1;34m'no unique mode; found %d equally common values'\u001b[0m \u001b[1;33m%\u001b[0m \u001b[0mlen\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mtable\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    507\u001b[0m                 )\n\u001b[0;32m    508\u001b[0m     \u001b[1;32melse\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mStatisticsError\u001b[0m: no unique mode; found 6 equally common values"
     ]
    }
   ],
   "source": [
    "#mode\n",
    "statistics.mode(nume)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'statics' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-18-bac1111f792c>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m()\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[1;31m#mode\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      2\u001b[0m \u001b[0mnume\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;36m1\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;36m5\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;36m12\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;36m33\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;36m46\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;36m33\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;36m21\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 3\u001b[1;33m \u001b[0mstatics\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mmode\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mnume\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m: name 'statics' is not defined"
     ]
    }
   ],
   "source": [
    "#mode\n",
    "nume=[1,5,12,33,46,33,21]\n",
    "statics.mode(nume)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'statics' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-19-f5f172af326c>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m()\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[1;31m#mode\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      2\u001b[0m \u001b[0mnume\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;36m1\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;36m5\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;36m12\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;36m33\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;36m46\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;36m33\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;36m2\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 3\u001b[1;33m \u001b[0mstatics\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mmode\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mnume\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m: name 'statics' is not defined"
     ]
    }
   ],
   "source": [
    "#mode\n",
    "nume=[1,5,12,33,46,33,2]\n",
    "statics.mode(nume)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "33"
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#mode\n",
    "nume=[1,5,12,33,46,33,2]\n",
    "statistics.mode(nume)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [],
   "source": [
    "#StatisticsError: no unique mode; found 6 equally common values\n",
    "#StatisticsError：ユニークモードはありません。 6つの同じような共通の値が見つかりました\n",
    "#この場合、３３が一番登場しているから問題ないはずだが…\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "False"
      ]
     },
     "execution_count": 22,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import keyword\n",
    "\n",
    "keyword.iskeyword(\"for\")\n",
    "keyword.iskeyword(\"football\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 23,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import keyword\n",
    "\n",
    "keyword.iskeyword(\"for\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "False"
      ]
     },
     "execution_count": 24,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import keyword\n",
    "\n",
    "keyword.iskeyword(\"football\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [],
   "source": [
    "def print_hell():\n",
    "    print(\"Hello\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [
    {
     "ename": "ModuleNotFoundError",
     "evalue": "No module named 'hello'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mModuleNotFoundError\u001b[0m                       Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-26-46f12b6b77c1>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m()\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[1;32mimport\u001b[0m \u001b[0mhello\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      2\u001b[0m \u001b[0mhello\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mprint_halo\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mModuleNotFoundError\u001b[0m: No module named 'hello'"
     ]
    }
   ],
   "source": [
    "import hello\n",
    "hello.print_halo()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [
    {
     "ename": "ModuleNotFoundError",
     "evalue": "No module named 'hello'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mModuleNotFoundError\u001b[0m                       Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-27-f0b8966c1ce4>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m()\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[1;32mimport\u001b[0m \u001b[0mhello\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      2\u001b[0m \u001b[0mhello\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mprint_hello\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mModuleNotFoundError\u001b[0m: No module named 'hello'"
     ]
    }
   ],
   "source": [
    "import hello\n",
    "hello.print_hello()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {},
   "outputs": [
    {
     "ename": "ModuleNotFoundError",
     "evalue": "No module named 'hello'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mModuleNotFoundError\u001b[0m                       Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-28-f0b8966c1ce4>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m()\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[1;32mimport\u001b[0m \u001b[0mhello\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      2\u001b[0m \u001b[0mhello\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mprint_hello\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mModuleNotFoundError\u001b[0m: No module named 'hello'"
     ]
    }
   ],
   "source": [
    "import hello\n",
    "hello.print_hello()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {},
   "outputs": [],
   "source": [
    "def print_hello():\n",
    "    print(\"Hello\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {},
   "outputs": [
    {
     "ename": "ModuleNotFoundError",
     "evalue": "No module named 'hello'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mModuleNotFoundError\u001b[0m                       Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-30-f0b8966c1ce4>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m()\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[1;32mimport\u001b[0m \u001b[0mhello\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      2\u001b[0m \u001b[0mhello\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mprint_hello\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mModuleNotFoundError\u001b[0m: No module named 'hello'"
     ]
    }
   ],
   "source": [
    "import hello\n",
    "hello.print_hello()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {},
   "outputs": [],
   "source": [
    "def print_hello():\n",
    "    print(\"Hello\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "metadata": {},
   "outputs": [
    {
     "ename": "ModuleNotFoundError",
     "evalue": "No module named 'hello'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mModuleNotFoundError\u001b[0m                       Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-32-f0b8966c1ce4>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m()\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[1;32mimport\u001b[0m \u001b[0mhello\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      2\u001b[0m \u001b[0mhello\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mprint_hello\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mModuleNotFoundError\u001b[0m: No module named 'hello'"
     ]
    }
   ],
   "source": [
    "import hello\n",
    "hello.print_hello()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Hello\n"
     ]
    }
   ],
   "source": [
    "#code in module\n",
    "print(\"Hello\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Hello\n"
     ]
    }
   ],
   "source": [
    "#code in module1\n",
    "print(\"Hello\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "metadata": {},
   "outputs": [
    {
     "ename": "ModuleNotFoundError",
     "evalue": "No module named 'module1'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mModuleNotFoundError\u001b[0m                       Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-35-138eb375ea7a>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m()\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[1;31m#code is module2\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 2\u001b[1;33m \u001b[1;32mimport\u001b[0m \u001b[0mmodule1\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;31mModuleNotFoundError\u001b[0m: No module named 'module1'"
     ]
    }
   ],
   "source": [
    "#code is module2\n",
    "import module1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "metadata": {},
   "outputs": [],
   "source": [
    "def print_hello():\n",
    "    print(\"Hello\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "metadata": {},
   "outputs": [
    {
     "ename": "ModuleNotFoundError",
     "evalue": "No module named 'hello'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mModuleNotFoundError\u001b[0m                       Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-37-f0b8966c1ce4>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m()\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[1;32mimport\u001b[0m \u001b[0mhello\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      2\u001b[0m \u001b[0mhello\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mprint_hello\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mModuleNotFoundError\u001b[0m: No module named 'hello'"
     ]
    }
   ],
   "source": [
    "import hello\n",
    "hello.print_hello()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "metadata": {},
   "outputs": [],
   "source": [
    "# -- test.py --\n",
    "def helloworld():\n",
    "    print(\"Hello World!\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "Missing parentheses in call to 'print'. Did you mean print(str)? (<ipython-input-39-b15aaf33c7da>, line 3)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  File \u001b[1;32m\"<ipython-input-39-b15aaf33c7da>\"\u001b[1;36m, line \u001b[1;32m3\u001b[0m\n\u001b[1;33m    print str\u001b[0m\n\u001b[1;37m            ^\u001b[0m\n\u001b[1;31mSyntaxError\u001b[0m\u001b[1;31m:\u001b[0m Missing parentheses in call to 'print'. Did you mean print(str)?\n"
     ]
    }
   ],
   "source": [
    "class Test:\n",
    "    def sayStr(self, str):\n",
    "        print str\n",
    " \n",
    "if __name__ == '__main__':\n",
    "    test = Test()\n",
    "    test.sayStr(\"Hello\")   # Hello"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "Missing parentheses in call to 'print'. Did you mean print(str)? (<ipython-input-40-b15aaf33c7da>, line 3)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  File \u001b[1;32m\"<ipython-input-40-b15aaf33c7da>\"\u001b[1;36m, line \u001b[1;32m3\u001b[0m\n\u001b[1;33m    print str\u001b[0m\n\u001b[1;37m            ^\u001b[0m\n\u001b[1;31mSyntaxError\u001b[0m\u001b[1;31m:\u001b[0m Missing parentheses in call to 'print'. Did you mean print(str)?\n"
     ]
    }
   ],
   "source": [
    "class Test:\n",
    "    def sayStr(self, str):\n",
    "        print str\n",
    " \n",
    "if __name__ == '__main__':\n",
    "    test = Test()\n",
    "    test.sayStr(\"Hello\")   # Hello"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "metadata": {},
   "outputs": [],
   "source": [
    "def add(a, b):\n",
    "    return a + b\n",
    "\n",
    "def sub(a, b):\n",
    "    return a - b"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "metadata": {},
   "outputs": [
    {
     "ename": "ModuleNotFoundError",
     "evalue": "No module named 'mymath'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mModuleNotFoundError\u001b[0m                       Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-42-90d6f8472784>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m()\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[1;32mimport\u001b[0m \u001b[0mmymath\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      2\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      3\u001b[0m \u001b[1;32mif\u001b[0m \u001b[0m__name__\u001b[0m \u001b[1;33m==\u001b[0m \u001b[1;34m'__main__'\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      4\u001b[0m     \u001b[0mprint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mmymath\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0madd\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;36m1\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;36m2\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      5\u001b[0m     \u001b[0mprint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mmymath\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0msub\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;36m1\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;36m2\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mModuleNotFoundError\u001b[0m: No module named 'mymath'"
     ]
    }
   ],
   "source": [
    "import mymath\n",
    "\n",
    "if __name__ == '__main__':\n",
    "    print(mymath.add(1, 2))\n",
    "    print(mymath.sub(1, 2))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "metadata": {},
   "outputs": [
    {
     "ename": "ModuleNotFoundError",
     "evalue": "No module named 'mymath'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mModuleNotFoundError\u001b[0m                       Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-43-90d6f8472784>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m()\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[1;32mimport\u001b[0m \u001b[0mmymath\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      2\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      3\u001b[0m \u001b[1;32mif\u001b[0m \u001b[0m__name__\u001b[0m \u001b[1;33m==\u001b[0m \u001b[1;34m'__main__'\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      4\u001b[0m     \u001b[0mprint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mmymath\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0madd\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;36m1\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;36m2\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      5\u001b[0m     \u001b[0mprint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mmymath\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0msub\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;36m1\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;36m2\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mModuleNotFoundError\u001b[0m: No module named 'mymath'"
     ]
    }
   ],
   "source": [
    "import mymath\n",
    "\n",
    "if __name__ == '__main__':\n",
    "    print(mymath.add(1, 2))\n",
    "    print(mymath.sub(1, 2))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
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
   "version": "3.7.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
