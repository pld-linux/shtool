Summary:	GNU shtool - the GNU Portable Shell Tool
Summary(pl):	GNU shtool - przeno¶ne narzêdzie pow³okowe GNU
Name:		shtool
Version:	2.0.1
Release:	2
License:	GPL
Group:		Development/Tools
Source0:	ftp://ftp.gnu.org/gnu/shtool/%{name}-%{version}.tar.gz
# Source0-md5:	b434ed054fed53af682b52489c7931d4
Patch0:		%{name}-tempfile.patch
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

%description -l pl
GNU shtool to kompilacja ma³ych, ale bardzo stabilnych i przeno¶nych
skryptów pow³oki w jedno narzêdzie pow³okowe. Wszystkie sk³adniki by³y
u¿ywane z powodzeniem przez wiele lat w wielu projektach
wolnodostêpnego oprogramowania. Scalony program shtool ma byæ u¿ywany
wewn±trz drzer ¼róde³ innych pakietów wolnodostêpnego oprogramowania.
Tam mo¿e przejmowaæ ró¿ne (zwykle nie przeno¶ne) zadania zwi±zane z
budowaniem i instalowaniem pakietu. W szczególno¶ci mo¿e zast±piæ
stare mkdir.sh, install.sh i powi±zane skrypty.

%prep
%setup -q
%patch0 -p1

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
