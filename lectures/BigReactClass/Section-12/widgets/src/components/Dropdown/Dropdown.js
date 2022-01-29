import React, { useState, useEffect, useRef } from 'react';

const Dropdown = ({ options, selected, onSelectedChange }) => {

    const [open, setOpen] = useState(false);
    const ref = useRef();

    /* When the component is mounted, it adds a click event listener to the body element. When the
    component is unmounted, it removes the event listener. */
    useEffect(() => {
        const onBodyClick = (event) => {
            if (ref.current.contains(event.target)) {
                return;
            }
            setOpen(false);
        };

        document.body.addEventListener("click", onBodyClick, { capture: true });

        return () => {
            document.body.removeEventListener("click", onBodyClick, {
                capture: true,
            });
        };
    }, []);

    const renderedOptions = options.map((option, index) => {

        /* If the value of the selected option is the same as the value of the option we're rendering,
        then we return null. Otherwise, we return a div with the label of the option and a click
        handler that will call the onSelectedChange function with the JSON stringified version of the
        option. */
        if (option.value === JSON.parse(selected).value) {
            return null
        } else {
            return (
                <div
                    key={index}
                    className='item'
                    onClick={() => onSelectedChange(JSON.stringify(option))}>
                    {option.label}
                </div>
            );
        }
    });

    return (
        <div className='ui form' ref={ref}>
            <div className='field'>
                <label className='label'>Select a Color</label>
                <div
                    className={`ui selection dropdown ${open ? 'visible active' : ''}`}
                    onClick={() => setOpen(!open)}>
                    <i className='dropdown icon'></i>
                    <div className='text'>{JSON.parse(selected).label}</div>
                    <div className={`menu ${open ? 'visible transition' : ''}`}>
                        {renderedOptions}
                    </div>
                </div>
            </div>
        </div >
    );
}

export default Dropdown;