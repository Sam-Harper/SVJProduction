This is the set of instructions to run at RAL. It supplements the generic README.md

## Area  Setup


For Run 2 ultra-legacy MC production (2016APV, 2016, 2017, 2018), `CMSSW_10_6_29_patch1` is used.

To setup the area for condor submission do the commands below

```bash
#release setup (part1)
mkdir SVJ # or whatever you want to call the directory 
cd SVJ
wget https://raw.githubusercontent.com/cms-svj/SVJProduction/Run2_UL/setup.sh
chmod +x setup.sh
./setup.sh -f Sam-Harper -b Run2_UL_RAL
#call host setup (part 2)
git clone https://github.com/FNALLPC/lpc-scripts
mkdir call_host_dir #where it will make the pipes
#proxy setup (part 3)
voms-proxy-init -voms cms -valid 192:00
cp /tmp/x509up_u$UID ./
```

Part 1: will create a CMSSW release in the directory `CMSSW_10_6_29_patch1` and checkout the necessary packages into it.

The as CMSSW_10_6_29_patch1 redhat 7 to run and diven redhat 7 is no longer supported, we have to run it in a container as described in the [cms-sw.github.io/singularity.html](https://cms-sw.github.io/singularity.html) using the cmssw:el7 image. However this container will not have some tools such as condor that we need. 
 
Thus we need to send forward those commands to the host machine for it to run and thus we use the useful script [call_host.sh](https://github.com/FNALLPC/lpc-scripts/blob/master/call_host.sh) to do this. We do this in part 2

Part 2: setups up this script and the directory needed for it to store the pipes

Finally we need to get the grid proxy in an area condor can read it and ship it with a job to be able to interact with remote CMS resources (eg reading tar balls, writing out root files). This is done in part 3 

Part 3: sets up the grid proxy and copies it to the current directory.

## Setting up the environment for submission



On the host machine we need to setup the call_host.sh script. We also need to set the X509_USER_PROXY environment variable on the host as the condor commands which look for this variable will be run on the host machine due to call_host.sh

Then we will enter the container and setup the environment there before running the production script

```bash
#first setup the environment on the host
export CALL_HOST_DIR=$PWD/call_host_dir
export CALL_HOST_STATUS=enable
export X509_USER_PROXY=$PWD/x509up_u$UID
cmssw-el7 #now enter the container
source /cvmfs/cms.cern.ch/cmsset_default.sh
export X509_USER_PROXY=$PWD/x509up_u$UID #also set this up in the container
cd CMSSW_10_6_29_patch1/src/SVJ/Production
cmsenv
voms-proxy-init --voms cms --valid 192:00 #if needed
test/lnbatch.sh myProduction #creates a new production directory so you can have multiple productions, skip if already setup
cd myProduction # go into the production directory
#now run the production an example is
python submitJobs.py -p -o root://mover.pp.rl.ac.uk///pnfs/pp.rl.ac.uk/data/cms/store/user/sharper/SVJ -d signalsV3_1.py -E 10 -N 1 --outpre step_GEN-SIM --config step_GEN-SIM -s --year 2016 --cmssw-container /cvmfs/unpacked.cern.ch/registry.hub.docker.com/cmssw/el7:x86_64/
```







