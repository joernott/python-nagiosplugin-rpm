# python-nagiosplugin-rpm
This repository provides the specfile for the python-nagiosplugin library. It
has been tested on RHEL 7 and CentOS 7 but might work on other redhat
derivatives as well.

It is based on http://www.thesimplebrief.com/linux/python-nagiosplugin.spec
which I found via https://bugzilla.redhat.com/show_bug.cgi?id=1057454. I tried
to fix the todos mentioned in the ticket. As python3 is finally mainstream, I
removed the conditionals around the python3 build.

## Credits
- Jordan Metzmeier for the initial spec file for 1.2
- [The people behind nagiosplugin](https://bitbucket.org/flyingcircus/nagiosplugin/src/default/CONTRIBUTORS.txt)
