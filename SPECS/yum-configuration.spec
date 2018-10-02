Name:           yum-configuration
Version:        1
Release:        0
Summary:        A BASH script to help maintain configuration control over Linux machines

Group:          TecAdmin
BuildArch:      noarch
License:        MIT
URL:            https://github.com/taz77/yum-configuration-management
Source0:        yum-configuration-1.0.tar.gz

%description
A simple BASH script with a configuration file that dumps a yum list to a text file with the date and IP address as part of the filename.

%prep
%setup -q
%build
%install
install -m 0755 -d $RPM_BUILD_ROOT/etc/yum-configuration
install -m 0644 yum-configuration-output.conf $RPM_BUILD_ROOT/etc/yum-configuration/yum-configuration-output.conf
install -m 0755 yum-configuration.sh $RPM_BUILD_ROOT/usr/lib/yum-configuration/yum-configuration.sh
install -m 0644 README.md $RPM_BUILD_ROOT/usr/lib/yum-configuration/README.md


%files
/etc/yum-configuration
/etc/yum-configuration/yum-configuration-output.conf
/usr/lib/yum-configuration/yum-configuration.sh


%changelog
* Tue Oct 02 2018 Brady Owens  1.0.0
  - Initial rpm release