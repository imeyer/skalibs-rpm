# skalibs rpm

Re-stumbled upon [s6](skarnet.org/software/s6) recently and saw they added a way for skarnet.org software to not have to install using the /package format. Here's my take on RPMs for skalibs on RHEL/CentOS 7.

### Building

Easy! Just do the following
```
git clone https://github.com/imeyer/skalibs-rpm
cd skalibs-rpm
bash ./build.sh
```
If that doesn't work, report an issue and I'll see what I can do.
