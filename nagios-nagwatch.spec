%include	/usr/lib/rpm/macros.perl
Summary:	Gtk-Perl frontend for viewing the current status of Nagios
Name:		nagios-nagwatch
Version:	0.1
Release:	0.2
License:	GPL
Group:		Applications
Source0:	nagwatch-%{version}.tar.gz
# Source0-md5:	815b34077f87ebceb1f5bf3a568138bd
Patch0:		nagwatch-path.patch
URL:		http://tinyurl.com/nmext
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdir	%{_datadir}/nagwatch

%description
Nagios Watch is a Gtk-Perl frontend, that reads the status.log file
which is created by Nagios <http://www.nagios.org>.

%prep
%setup -q -n nagwatch-%{version}
%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_appdir}}
cp -a *.xpm $RPM_BUILD_ROOT%{_appdir}
install nagwatch $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHOR CREDITS LICENSE README
%attr(755,root,root) %{_bindir}/nagwatch
%{_appdir}
