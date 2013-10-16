%define		plugin	birthdaypicker
Summary:	Attempts to mimic the functionality of the birthday select lists on the Facebook signup page
Name:		jquery-%{plugin}
Version:	1.4
Release:	1
License:	MIT/GPL
Group:		Applications/WWW
Source0:	https://github.com/abecoffman/birthdaypicker/archive/834bca8/%{plugin}-%{version}.tar.gz
# Source0-md5:	884c18cac5f36a26be0c7621e92ea071
URL:		https://github.com/abecoffman/birthdaypicker
Requires:	jquery
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdir	%{_datadir}/jquery/%{plugin}

%description
The birthday picker seeks to emulate the functionality of the birthday
picker on the Facebook signup page. It uses three select boxes to
choose a date, and tries to ensure that the date is valid by
accounting for leap years, etc...

It also has a number of options, making it somewhat customizable. The
birthday picker generates the following markup:

%package demo
Summary:	Demo for jQuery.%{plugin}
Summary(pl.UTF-8):	Pliki demonstracyjne dla pakietu jQuery.%{plugin}
Group:		Development
Requires:	%{name} = %{version}-%{release}

%description demo
Demonstrations and samples for jQuery.%{plugin}.

%prep
%setup -qc
mv birthdaypicker-*/* .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_appdir},%{_examplesdir}/%{name}-%{version}}

cp -p bday-picker.js $RPM_BUILD_ROOT%{_appdir}/%{plugin}-%{version}.js
cp -p bday-picker.min.js $RPM_BUILD_ROOT%{_appdir}/%{plugin}-%{version}.min.js
ln -s %{plugin}-%{version}.js $RPM_BUILD_ROOT%{_appdir}/%{plugin}.src.js
ln -s %{plugin}-%{version}.min.js $RPM_BUILD_ROOT%{_appdir}/%{plugin}.js
ln -s %{plugin}-%{version}.min.js $RPM_BUILD_ROOT%{_appdir}/%{plugin}.min.js

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md
%{_appdir}
