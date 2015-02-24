Summary:	GNU shtool - the GNU Portable Shell Tool
Summary(pl.UTF-8):	GNU shtool - przenośne narzędzie powłokowe GNU
Name:		shtool
Version:	2.0.8
Release:	2
License:	GPL v2+
Group:		Development/Tools
Source0:	http://ftp.gnu.org/gnu/shtool/%{name}-%{version}.tar.gz
# Source0-md5:	c5f7c6836882d48bc79049846a5f9c5b
URL:		http://www.gnu.org/software/shtool/
BuildRequires:	automake
BuildRequires:	perl-tools-pod
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNU shtool is a compilation of small but very stable and portable
shell scripts into a single shell tool. All ingredients were in
successful use over many years in various free software projects. The
compiled shtool program is intended to be used inside the source tree
of other free software packages. There it can overtake various
(usually non-portable) tasks related to the building and installation
of such a package. It especially can replace the old mkdir.sh,
install.sh and related scripts.

%description -l pl.UTF-8
GNU shtool to kompilacja małych, ale bardzo stabilnych i przenośnych
skryptów powłoki w jedno narzędzie powłokowe. Wszystkie składniki były
używane z powodzeniem przez wiele lat w wielu projektach
wolnodostępnego oprogramowania. Scalony program shtool ma być używany
wewnątrz drzew źródeł innych pakietów wolnodostępnego oprogramowania.
Tam może przejmować różne (zwykle nieprzenośne) zadania związane z
budowaniem i instalowaniem pakietu. W szczególności może zastąpić
stare mkdir.sh, install.sh i powiązane skrypty.

%prep
%setup -q

%build
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README THANKS
%attr(755,root,root) %{_bindir}/shtool
%attr(755,root,root) %{_bindir}/shtoolize
%{_datadir}/%{name}
%{_aclocaldir}/shtool.m4
%{_mandir}/man1/shtool.1*
%{_mandir}/man1/shtool-*.1*
%{_mandir}/man1/shtoolize.1*
