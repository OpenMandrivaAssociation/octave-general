%define	pkgname general

Summary:	General tools for Octave
Name:       octave-%{pkgname}
Version:	1.2.2
Release:        6
Source0:	%{pkgname}-%{version}.tar.gz
License:	GPLv3+
Group:		Sciences/Mathematics
Url:		http://octave.sourceforge.net/general/
Conflicts:	octave-forge <= 20090607
Requires:	octave >= 3.2.4
BuildRequires:  octave-devel >= 3.2.4
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glu)
Requires:       octave(api) = %{octave_api}
Requires(post): octave
Requires(postun): octave

%description
General tools for Octave. String dictionary, parallel computing.

%prep
%setup -q -c %{pkgname}-%{version}
cp %{SOURCE0} .

%install
%__install -m 755 -d %{buildroot}%{_datadir}/octave/packages/
%__install -m 755 -d %{buildroot}%{_libdir}/octave/packages/
export OCT_PREFIX=%{buildroot}%{_datadir}/octave/packages
export OCT_ARCH_PREFIX=%{buildroot}%{_libdir}/octave/packages
octave -q --eval "pkg prefix $OCT_PREFIX $OCT_ARCH_PREFIX; pkg install -verbose -local %{pkgname}-%{version}.tar.gz"

tar zxf %{SOURCE0} 
mv %{pkgname}/COPYING .
mv %{pkgname}/DESCRIPTION .

%clean

%post
%octave_cmd pkg rebuild

%preun
%octave_pkg_preun

%postun
%octave_cmd pkg rebuild

%files
%doc COPYING DESCRIPTION
%{_datadir}/octave/packages/%{pkgname}-%{version}
%{_libdir}/octave/packages/%{pkgname}-%{version}
