#Homework 1
import pexpect

newprimates = open("primates2.nex","w")
oldprimates = open("primates.nex").read()

#replace mcmc with mcmcp
corrected = oldprimates.replace("mcmc", "mcmcp")

#check the location to make sure it was properly replaced 
corrected.find("mcmcp")
oldprimates.find("mcmc")

#write corrected string to the newprimates file
#can use write or writelines
newprimates.write(corrected)

#close file
newprimates.close()

child = pexpect.spawn("mb -i primates2.nex")
child.sendline(r"mcmc")
#tell mrbayes to stop the analysis
child.sendline("no")
child.expect("MrBayes >")
#shows all of the screen output
print child.before

#tell mrbayes to quit
child.sendline("quit")
#check that it quit
child.isalive()


#Homework 2
#spawn an interactive mrbayes process
child = pexpect.spawn("mb -i primates2.nex")
#send the command "execute primates2.nex" to mrbayes
child.sendline(r"execute primates2.nex")
#send to sumt command to mrbayes
child.sendline("sumt")
#check to see that the mrbayes command prompt is returned 
child.expect("MrBayes >")
#print everything before the mrbayes prompt
print child.before
#send the sump command
child.sendline("sump")
#quit mrbayes
child.sendline("quit")



import glob
#returns a list of all files in the current directory
allfiles = glob.glob("*")
#files that start with is in /usr/bin
s_usr_bin = glob.glob("/usr/bin/s*")
#list of image files in current directory
images = glob.glob("*.jpg")

import glob, pexpect
nexus_files=glob.glob("*.nex")
for nex in nexus_files:
	output = pexpect.run("mb nex")



#Homework 3
#write a function that takes a nexus file and a numgen variable to interactively start mrbayes
import os
#where my primate files live
os.chdir("/home/vagrant/sandbox")
#function to start a mrbayes run with fname for ngen generations
def mbRunner(fname, ngen = 5000):
    child = pexpect.spawn("mb -i {}".format(fname))
    child.sendline(r"set nowarn = yes")
    child.expect("MrBayes >")
    child.sendline(r"mcmcp ngen = {}".format(ngen))
    child.expect("MrBayes >")
    child.sendline(r"mcmc")
    child.sendline(r"no")
    child.expect("MrBayes >")
    child.sendline(r"quit")

#part 2
def sumRunner(fname):
	#this function uses mrbayes to run sump and sumt
	child = pexpect.spawn("mb -i")
	child.sendline(r"execute {}".format(fname))
	child.expect("MrBayes >")
	child.sendline(r"set nowarn = yes")
	child.expect("MrBayes >")
	child.sendline(r"sumt")
	child.expect("MrBayes >")
	child.sendline(r"sump")
	child.expect("MrBayes >")
	child.sendline(r"quit")

#part 3
import glob

beforeFF = glob.glob("*.*")
beforeTreeFF = glob.glob("*.t")

runFF = "primtates2.nex"

print "Before there were {} files in the directory and {} than end in '.t'".format(len(beforeFF), len(beforeTreeFF))


mbRunner(runFF, 6000)
sumRunner(runFF)

afterFF = glob.glob("*.*")
print "Now there are {} files in the directory and {} than end in '.t'".format(len(afterFF), len(glob.glob("*.t")))
afterTree = glob.glob("*.t")
print "The tree files are: " + ", ".join(afterTree) + "."



