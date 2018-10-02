# Yum Configuration Management Script

Small script package that can be used to help with configuration management of Linux machines that can be packaged as an rpm for private deployment.

The purpose of the package is to aid in the confirmation management of RHEL based Linux machines or any distribution that uses YUM.

# Building RPM

To build this RPM you need to have the RPMbuild and RPMdevtools installed.
  `yum install rpm-build rpmdevtools`
Enter the SOURCES folder and and create a tarball of the package for the RPM to use in build
  - `cd SOURCES`
  - `tar -czf yum-configuration-1.0.tar.gz yum-configuration-1`

Return to the root of this repo
- `cd ..`
- `rpmbuild -ba SPECS/yum-configuration.spec`

The output of this will be an RPM in `./RPMS/noarch/` named `yum-configuration-1-0.noarch.rpm`. The RPM can then be either deployed to a local YUM server or installed via `rpm -ivh yum-configuration-1-0.noarch.rpm`

# Usage

Modify the configuration file /etc/yum-configuration/yum-configuration-output.conf before running this script. The configuration file will define the destination of the reports and the name of the ethernet device on the machine that is being used to identify the reports.

Once configured, this script can be run manually or via cron.