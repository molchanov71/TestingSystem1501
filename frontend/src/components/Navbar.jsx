import React from 'react';


const Navbar = ({options}) =>
{
    return (
        <div className="Navbar">
            {
                options.map(opt => 
                    opt.active
                        ? <span className="NavbarElement" key={opt.id}>{opt.name}</span>
                        : <a href={opt.link} className="NavbarElement NavbarLink" key={opt.id}>{opt.name}</a>
                )
            }
        </div>
    )
}

export default Navbar; 